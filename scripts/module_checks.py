"""Source-retention checks; these do not execute agent or page evaluations."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


MODULE = "modules/landing-pages/"
TOPICS = (
    "GUIDE.md", "entry-and-navigation.md", "content-and-trust.md",
    "interaction-and-demonstrations.md", "technical-quality.md", "validation.md",
)


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def validate_landing_module(root: Path) -> list[str]:
    errors: list[str] = []
    try:
        matrix = json.loads((root / MODULE / "traceability.json").read_text(encoding="utf-8"))
        scenarios = json.loads((root / "evals/landing-pages/cases.json").read_text(encoding="utf-8"))
        core = json.loads((root / "evals/evals.json").read_text(encoding="utf-8"))
        if matrix["module_version"] != "0.4.0" or matrix["integration_revision"] != 1:
            errors.append("ULPG traceability version mismatch")
        if matrix["behavioral_non_regression"] != "unverified":
            errors.append("ULPG behavioral status needs executed comparison evidence")
        sections: dict[int, tuple[str, str]] = {}
        for filename in TOPICS:
            rel = MODULE + filename
            text = (root / rel).read_text(encoding="utf-8")
            headings = list(re.finditer(r"^## (\d+)\. .+$", text, re.M))
            for index, heading in enumerate(headings):
                number = int(heading[1])
                end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
                content = text[heading.start():end].strip() + "\n"
                if number in sections:
                    errors.append(f"ULPG section {number} has duplicate authorities")
                sections[number] = (rel, content)
        rows = matrix["sections"]
        if [row["section"] for row in rows] != list(range(1, 21)) or set(sections) != set(range(1, 21)):
            errors.append("ULPG must retain exactly twenty mapped source sections")
        actual_requirements = []
        for row in rows:
            number = row["section"]
            if number not in sections:
                continue
            rel, content = sections[number]
            if row["authority"] != rel or row["normalized_utf8_sha256"] != sha(content):
                errors.append(f"ULPG source retention failed for section {number}")
            subsection = str(number)
            for line_number, line in enumerate(content.splitlines(), 1):
                heading = re.match(r"### (\d+\.\d+)", line)
                if heading:
                    subsection = heading[1]
                levels = re.findall(r"\b(?:MUST NOT|MUST|SHOULD|MAY)\b", line)
                inherited = number == 16 and line.startswith("- ")
                if inherited:
                    levels = ["MUST NOT"]
                if levels:
                    actual_requirements.append({
                        "id": f"ULPG-0.4.0-{subsection}-L{line_number}",
                        "source_section": subsection,
                        "section_line": line_number,
                        "levels": levels,
                        "line_sha256": sha(line),
                        "authority": rel,
                        "inherited_level": inherited,
                    })
        if matrix["requirements"] != actual_requirements:
            errors.append("ULPG normative requirement mappings or levels differ from the source matrix")
        if sum(row["inherited_level"] for row in actual_requirements) != 7:
            errors.append("ULPG must retain all seven inherited non-regression prohibitions")
        # The original seventeen cases may be extended, but not rewritten.
        original_cases = json.dumps(core["evals"][:17], sort_keys=True, ensure_ascii=True)
        if sha(original_cases) != matrix["ddm_baseline_cases_sha256"]:
            errors.append("DDM original seventeen evaluation cases changed")
        cases = scenarios["evals"]
        if scenarios["skill_name"] != "design-decision-method" or len(cases) != 5:
            errors.append("combined suite must contain the five fictional source scenarios")
        if [case["id"] for case in cases] != list(range(1, 6)):
            errors.append("combined scenario ids must be consecutive 1–5")
        for case in cases:
            if not all(isinstance(case.get(key), str) and case[key].strip() for key in ("prompt", "expected_output")):
                errors.append(f"combined case {case.get('id')} is missing performer/grader fields")
            if not isinstance(case.get("files"), list) or not isinstance(case.get("expectations"), list) or not case["expectations"]:
                errors.append(f"combined case {case.get('id')} has invalid files or expectations")
            if "expected_output" in case["prompt"] or "Grader only" in case["prompt"]:
                errors.append(f"combined case {case.get('id')} leaks grader fields into the prompt")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"landing-pages module validation: {exc}")
    return errors
