# Merge comparison protocol

Candidate: DDM 2.4.0 with ULPG 0.4.0 integration revision 1. DDM baseline: 2.3.0 at 5fab8fd00a9feb8f020e81a697aeaad35d43dfdd. ULPG baseline: 0.4.0 at a42a2faa0b097639f96e4a3e9c3d399084ebadcf.

## Suite A — DDM preservation

Keep all seventeen cases in evals/evals.json byte-identical to 2.3.0. Run each against baseline and candidate in separate fresh contexts with matched model/settings/tools/raw brief. Give performers only the prompt and supplied raw files, never expected_output or expectations. Case 10 uses normal automatic discovery without explicitly invoking or loading DDM. Grade original criteria individually; investigate every regression rather than averaging it away. Record actual loaded references, map timing, system preservation, scope proportionality, unrelated-task overhead and evidence honesty.

## Suite B — ULPG source preservation

Run scripts/validate_release.py. Its section hashes and requirement-line checks cover all twenty original sections, MUST/SHOULD/MAY wording, scoped context and the seven inherited non-regression prohibitions. Compare traceability.json to the pinned source when auditing provenance. These automated checks establish retention of imported wording, not behavioral conformance or external standards compliance.

## Suite C — combined behavior

Use the same five unchanged fictional briefs in cases.json against standalone DDM 2.3.0, standalone ULPG 0.4.0 (original guide and agent workflow), and the combined candidate. Fresh independent contexts must not receive another condition's output or grader expectations. All conditions get the same brief and accessible raw evidence; record the instructions loaded for each. Grade entry/discovery rationale, first-time/returning scope, demo integrity/fallbacks, freshness, technical evidence boundaries and all shared DDM safeguards. The source scenario comparison is historical heuristic documentation evidence only.

For every run save the condition/version, model/settings, tools, prompt, raw inputs, reference scope, actual output, timing, token count or labeled length proxy, per-criterion grade/rationale, and limitations. Save reports in evals/output/ (ignored), or outside the package. Separate proposal, heuristic, automated, manual and user-research evidence. New pages require separate implementation checks and user evidence before claiming measured page outcomes.

## Current status and release gate

Suite A: original cases preserved; paired behavioral runs unrun.
Suite B: automated source-retention checks available; run results belong in the execution report.
Suite C: five fixtures prepared; all fifteen condition/scenario runs unrun.

This candidate cannot be labeled behaviorally non-regressing or used as evidence to retire the independent ULPG repository until matched comparisons have been executed and unresolved regressions addressed. Package integrity is separate from behavioral results.
