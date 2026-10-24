"""Show that validation accepts the release and rejects a broken copy."""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

from release_lib import INCLUDE_FILES, MANIFEST_NAME, SKILL_DIR, validate_release, write_manifest
from package_release import archive_bytes


def copy_release(source: Path, dest: Path) -> None:
    for rel in (*INCLUDE_FILES, MANIFEST_NAME):
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source / rel, target)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_release(root)
    require(not errors, "clean tree failed validation:\n" + "\n".join(errors))

    with tempfile.TemporaryDirectory() as temp_name:
        temp = Path(temp_name)
        altered = temp / "altered"
        copy_release(root, altered)
        runtime_output = altered / "evals/output/comparison.json"
        runtime_output.parent.mkdir(parents=True)
        runtime_output.write_text('{"status": "unrun"}', encoding="utf-8")
        require(not validate_release(altered), "ignored evaluation evidence was treated as package content")
        skill = altered / "SKILL.md"
        skill.write_bytes(skill.read_bytes() + b"\n")
        altered_errors = validate_release(altered)
        require(bool(altered_errors), "an altered file was accepted")
        require(
            any("hash mismatch" in error or "canonical checksum" in error for error in altered_errors),
            "an altered file was not reported as a checksum failure",
        )

        missing = temp / "missing"
        copy_release(root, missing)
        (missing / "references" / "routing.md").unlink()
        missing_errors = validate_release(missing)
        require(bool(missing_errors), "a missing file was accepted")
        require(
            any("routing.md" in error for error in missing_errors),
            "a missing file was not named in the errors",
        )

        evaluations = temp / "evaluations"
        copy_release(root, evaluations)
        eval_path = evaluations / "evals" / "evals.json"
        eval_doc = json.loads(eval_path.read_text(encoding="utf-8"))
        extra = dict(eval_doc["evals"][-1], id=len(eval_doc["evals"]) + 1)
        eval_doc["evals"].append(extra)
        eval_path.write_bytes((json.dumps(eval_doc, indent=2) + "\n").encode("utf-8"))
        write_manifest(evaluations)
        require(not validate_release(evaluations), "an additional consecutive evaluation was rejected")

        eval_doc["evals"][-1]["id"] = eval_doc["evals"][-2]["id"]
        eval_path.write_bytes((json.dumps(eval_doc, indent=2) + "\n").encode("utf-8"))
        write_manifest(evaluations)
        require(
            any("ids must be consecutive" in error for error in validate_release(evaluations)),
            "a duplicate evaluation id was accepted",
        )

        eval_doc["evals"] = eval_doc["evals"][:10]
        eval_path.write_bytes((json.dumps(eval_doc, indent=2) + "\n").encode("utf-8"))
        write_manifest(evaluations)
        require(
            any("expected at least 17" in error for error in validate_release(evaluations)),
            "missing landing-page evaluations were accepted",
        )

        module = temp / "module"
        copy_release(root, module)
        topic = module / "modules/landing-pages/interaction-and-demonstrations.md"
        original = topic.read_text(encoding="utf-8")
        topic.write_bytes(original.replace(
            "- **MUST:** Distinguish simulated completion from real execution in feedback as well as initial labels.",
            "- **SHOULD:** Distinguish simulated completion from real execution in feedback as well as initial labels.",
        ).encode("utf-8"))
        write_manifest(module)
        require(
            any("source retention failed" in error for error in validate_release(module)),
            "weakened demonstration requirement survived manifest regeneration",
        )
        topic.write_bytes(original.encode("utf-8"))

        entry = module / "modules/landing-pages/GUIDE.md"
        original_entry = entry.read_text(encoding="utf-8")
        entry.write_bytes(original_entry.replace(
            "(templates/page-brief.md)", "(templates/nonexistent.md)",
        ).encode("utf-8"))
        write_manifest(module)
        require(
            any("unpackaged resource" in error for error in validate_release(module)),
            "broken nested module link was accepted",
        )
        entry.write_bytes(original_entry.encode("utf-8"))

        original_evals = module / "evals/evals.json"
        changed_cases = json.loads(original_evals.read_text(encoding="utf-8"))
        changed_cases["evals"][0]["prompt"] = "Replacement brief"
        original_evals.write_bytes((json.dumps(changed_cases) + "\n").encode("utf-8"))
        write_manifest(module)
        require(
            any("original seventeen" in error for error in validate_release(module)),
            "rewritten DDM baseline evaluation was accepted",
        )

        copy_release(root, module)
        template = module / "modules/landing-pages/templates/third-party-inventory.md"
        template.unlink()
        require(
            any("missing promised file" in error and "third-party-inventory" in error for error in validate_release(module)),
            "missing nested template was accepted",
        )

        payload = archive_bytes(root)
        archive_path = temp / f"{SKILL_DIR}.zip"
        archive_path.write_bytes(payload)
        with zipfile.ZipFile(archive_path) as archive:
            names = archive.namelist()
            require(all(name.startswith(f"{SKILL_DIR}/") for name in names), "export is missing the enclosing folder")
            for rel in (*INCLUDE_FILES, MANIFEST_NAME):
                archived = f"{SKILL_DIR}/{rel}"
                require(archived in names, f"export omitted {rel}")
                require(archive.read(archived) == (root / rel).read_bytes(), f"export bytes differ for {rel}")
            extracted = temp / "extracted"
            archive.extractall(extracted)
        require(not validate_release(extracted / SKILL_DIR), "export fails standalone validation")

    print("integrity checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
