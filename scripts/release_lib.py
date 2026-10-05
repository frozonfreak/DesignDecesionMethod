"""Shared release checks for Design Decision Method.

The canonical checksum is SHA-256 over sorted relative UTF-8 paths.
Each path is followed by a NUL byte, the exact file bytes, and another NUL.
release-manifest.json is excluded from that checksum and listed beside it.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover - exercised when the dependency is missing
    raise SystemExit(
        "PyYAML is required. Install it with: python -m pip install -r scripts/requirements.txt"
    ) from exc


MANIFEST_NAME = "release-manifest.json"
SKILL_DIR = "design-decision-method"
ALGORITHM = "SHA-256 of sorted relative UTF-8 paths, NUL, exact file bytes, NUL; excludes manifest"

# Explicit skill package. Repository scripts, CI, and VCS files are not included.
INCLUDE_FILES = (
    "CHANGELOG.md",
    "README.md",
    "SKILL.md",
    "agents/openai.yaml",
    "assets/design-record-template.md",
    "evals/evals.json",
    "references/acceptance-and-validation.md",
    "references/accessibility.md",
    "references/ai-interfaces.md",
    "references/modern-design.md",
    "references/routing.md",
    "references/sources.md",
    "references/visual-systems.md",
)

SCAN_DIRS = ("agents", "assets", "evals", "references")
LOCAL_REF = re.compile(
    r"(?<![A-Za-z0-9:/._~-])((?:references|assets|evals|agents)/[A-Za-z0-9_.-]+)"
)
VERSION_HEADING = re.compile(r"^## (\d+\.\d+\.\d+)\s+—", re.M)
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_bytes(root: Path, rel: str) -> bytes:
    return (root / rel).read_bytes()


def canonical_sha256(root: Path) -> str:
    digest = hashlib.sha256()
    for rel in sorted(INCLUDE_FILES):
        digest.update(rel.encode("utf-8"))
        digest.update(b"\0")
        digest.update(read_bytes(root, rel))
        digest.update(b"\0")
    return digest.hexdigest()


def file_hashes(root: Path) -> dict[str, str]:
    return {rel: sha256_bytes(read_bytes(root, rel)) for rel in sorted(INCLUDE_FILES)}


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("SKILL.md frontmatter is not closed")
    return text[4:end], text[end + 5 :]


def load_skill(root: Path) -> dict:
    text = (root / "SKILL.md").read_text(encoding="utf-8")
    raw, _body = split_frontmatter(text)
    loaded = yaml.safe_load(raw)
    if not isinstance(loaded, dict):
        raise ValueError("SKILL.md frontmatter must be a mapping")
    return loaded


def manifest_document(root: Path) -> dict:
    skill = load_skill(root)
    metadata = skill.get("metadata") or {}
    return {
        "version": metadata.get("version"),
        "updated": metadata.get("updated"),
        "canonical_sha256": canonical_sha256(root),
        "algorithm": ALGORITHM,
        "files": file_hashes(root),
    }


def dump_manifest(document: dict) -> str:
    return json.dumps(document, indent=2, ensure_ascii=True) + "\n"


def write_manifest(root: Path) -> None:
    text = dump_manifest(manifest_document(root))
    (root / MANIFEST_NAME).write_bytes(text.encode("utf-8"))


def package_members(root: Path) -> list[tuple[str, bytes]]:
    directories = {
        f"{SKILL_DIR}/",
        f"{SKILL_DIR}/agents/",
        f"{SKILL_DIR}/assets/",
        f"{SKILL_DIR}/evals/",
        f"{SKILL_DIR}/references/",
    }
    members = [(name, b"") for name in directories]
    for rel in (*INCLUDE_FILES, MANIFEST_NAME):
        members.append((f"{SKILL_DIR}/{rel}", read_bytes(root, rel)))
    members.sort(key=lambda item: item[0])
    return members


def validate_release(root: Path) -> list[str]:
    errors: list[str] = []
    root = root.resolve()

    for rel in (*INCLUDE_FILES, MANIFEST_NAME):
        path = root / rel
        if not path.is_file():
            errors.append(f"missing promised file: {rel}")
    if errors:
        return errors

    for rel in (*INCLUDE_FILES, MANIFEST_NAME):
        if b"\r\n" in read_bytes(root, rel):
            errors.append(f"CRLF line endings are not allowed in {rel}")

    for directory in SCAN_DIRS:
        base = root / directory
        if not base.is_dir():
            errors.append(f"missing directory: {directory}")
            continue
        for path in sorted(base.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(root).as_posix()
            if rel not in INCLUDE_FILES:
                errors.append(f"file is outside the canonical include set: {rel}")

    try:
        skill = load_skill(root)
    except Exception as exc:  # noqa: BLE001 - report parser failures as validation errors
        errors.append(f"SKILL.md frontmatter: {exc}")
        return errors

    name = skill.get("name")
    description = skill.get("description")
    if not isinstance(name, str) or not NAME_PATTERN.fullmatch(name) or len(name) > 64:
        errors.append("SKILL.md name must be 1-64 lowercase letters, numbers, and single hyphens")
    elif name != SKILL_DIR:
        errors.append(f"SKILL.md name must be {SKILL_DIR} so the packaged folder matches")
    if not isinstance(description, str) or not description.strip():
        errors.append("SKILL.md description must be a non-empty string")
    elif len(description) > 1024:
        errors.append(f"SKILL.md description is {len(description)} characters; the limit is 1024")

    compatibility = skill.get("compatibility")
    if compatibility is not None and (not isinstance(compatibility, str) or len(compatibility) > 500):
        errors.append("SKILL.md compatibility, when present, must be a string of at most 500 characters")

    metadata = skill.get("metadata")
    if not isinstance(metadata, dict):
        errors.append("SKILL.md metadata must be a mapping")
        metadata = {}
    else:
        for key, value in metadata.items():
            if not isinstance(key, str) or not isinstance(value, str):
                errors.append(f"SKILL.md metadata.{key} must be a string")

    allowed_tools = skill.get("allowed-tools")
    if allowed_tools is not None and not isinstance(allowed_tools, str):
        errors.append("SKILL.md allowed-tools, when present, must be a string")

    version = metadata.get("version") if isinstance(metadata, dict) else None
    updated = metadata.get("updated") if isinstance(metadata, dict) else None

    try:
        host = yaml.safe_load((root / "agents/openai.yaml").read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"agents/openai.yaml: {exc}")
        host = None
    if not isinstance(host, dict) or not isinstance(host.get("interface"), dict):
        errors.append("agents/openai.yaml must be a mapping with an interface mapping")
    else:
        interface = host["interface"]
        for key in ("display_name", "short_description", "default_prompt"):
            if not isinstance(interface.get(key), str) or not interface[key].strip():
                errors.append(f"agents/openai.yaml interface.{key} must be a non-empty string")

    try:
        manifest = json.loads((root / MANIFEST_NAME).read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"release-manifest.json: {exc}")
        manifest = None
    if not isinstance(manifest, dict):
        errors.append("release-manifest.json must be a JSON object")
        manifest = {}

    files = manifest.get("files")
    if not isinstance(files, dict):
        errors.append("release-manifest.json files must be an object")
        files = {}
    expected_keys = list(sorted(INCLUDE_FILES))
    actual_keys = list(files.keys())
    if actual_keys != expected_keys:
        errors.append("manifest coverage does not match the canonical include set")
    if manifest.get("algorithm") != ALGORITHM:
        errors.append("manifest algorithm text does not match the canonical convention")
    if manifest.get("version") != version:
        errors.append(
            f"version mismatch: SKILL.md metadata.version is {version!r}, manifest is {manifest.get('version')!r}"
        )
    if manifest.get("updated") != updated:
        errors.append(
            f"updated mismatch: SKILL.md metadata.updated is {updated!r}, manifest is {manifest.get('updated')!r}"
        )

    changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
    heading = VERSION_HEADING.search(changelog)
    if heading is None:
        errors.append("CHANGELOG.md is missing a ## version heading")
    elif heading.group(1) != version:
        errors.append(
            f"version mismatch: changelog starts at {heading.group(1)}, SKILL.md metadata.version is {version}"
        )
    if "six evaluation cases, not seven" not in changelog:
        errors.append("changelog must record that 2.1.0 contained six evaluation cases, not seven")

    readme = (root / "README.md").read_text(encoding="utf-8")
    if f"Current release: {version}." not in readme:
        errors.append(f"README.md must state Current release: {version}.")
    for rel in INCLUDE_FILES:
        if rel == "README.md":
            continue
        if Path(rel).name not in readme:
            errors.append(f"README.md contents do not mention {rel}")

    hashes = file_hashes(root)
    for rel, expected in hashes.items():
        recorded = files.get(rel)
        if recorded != expected:
            errors.append(f"hash mismatch for {rel}")
    canonical = canonical_sha256(root)
    if manifest.get("canonical_sha256") != canonical:
        errors.append("canonical checksum mismatch")

    try:
        evals_doc = json.loads((root / "evals/evals.json").read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"evals/evals.json: {exc}")
        evals_doc = None
    if not isinstance(evals_doc, dict):
        errors.append("evals/evals.json must be a JSON object")
    else:
        if evals_doc.get("skill_name") != name:
            errors.append("evals/evals.json skill_name must match SKILL.md name")
        cases = evals_doc.get("evals")
        if not isinstance(cases, list):
            errors.append("evals/evals.json evals must be an array")
            cases = []
        if len(cases) != 10:
            errors.append(f"expected 10 evaluation cases, found {len(cases)}")
        ids = []
        for case in cases:
            if not isinstance(case, dict):
                errors.append("each evaluation must be an object")
                continue
            ids.append(case.get("id"))
            prompt = case.get("prompt")
            if not isinstance(prompt, str) or not prompt.strip():
                errors.append(f"evaluation {case.get('id')} is missing a prompt")
                prompt = ""
            if not isinstance(case.get("expected_output"), str) or not case.get("expected_output").strip():
                errors.append(f"evaluation {case.get('id')} is missing expected_output")
            expectations = case.get("expectations")
            if (
                not isinstance(expectations, list)
                or not expectations
                or not all(isinstance(item, str) and item.strip() for item in expectations)
            ):
                errors.append(f"evaluation {case.get('id')} needs a non-empty expectations array")
            if not isinstance(case.get("files"), list):
                errors.append(f"evaluation {case.get('id')} files must be an array")
            if "expected_output" in prompt or "Grader only" in prompt:
                errors.append(f"evaluation {case.get('id')} puts grader text in the task prompt")
            if "invocation" in case and not isinstance(case.get("invocation"), str):
                errors.append(f"evaluation {case.get('id')} invocation must be a string")
        if ids != list(range(1, 11)):
            errors.append(f"evaluation ids must be 1 through 10 in order, found {ids}")
        logo = next((case for case in cases if isinstance(case, dict) and case.get("id") == 10), None)
        if isinstance(logo, dict):
            if logo.get("prompt") != "Design a logo for my bakery.":
                errors.append("case 10 prompt must be the logo brief alone")
            if logo.get("invocation") != "automatic":
                errors.append("case 10 must be an automatic-trigger test")
            for needle in ("design-decision-method", "Design Decision Method", "SKILL.md"):
                if needle in str(logo.get("prompt")):
                    errors.append("case 10 prompt must not invoke the method")

    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    template = (root / "assets/design-record-template.md").read_text(encoding="utf-8")
    visual = (root / "references/visual-systems.md").read_text(encoding="utf-8")
    if "Honour that request" not in skill_text:
        errors.append("selection precedence is missing from SKILL.md")
    if "smallest map that is sufficient" not in skill_text or "smallest sufficient map" not in template:
        errors.append("the object-map fallback must be the smallest sufficient map")
    if "three-row" in skill_text or "three-row" in template:
        errors.append("the fixed three-row map fallback is still present")
    if "one or two key moments" in visual:
        errors.append("visual emphasis still uses a per-screen quota")
    if "compact direction statement" not in skill_text:
        errors.append("presentation direction scope is missing from SKILL.md")

    seen: set[str] = set()
    for rel in (*INCLUDE_FILES,):
        if not rel.endswith((".md", ".yaml", ".json")):
            continue
        text = (root / rel).read_text(encoding="utf-8")
        for match in LOCAL_REF.findall(text):
            if "<" in match or match in seen:
                continue
            seen.add(match)
            if match not in INCLUDE_FILES:
                errors.append(f"{rel} references missing local resource {match}")

    return errors
