# Sources and verification

Use these official entry points to look up exact rules. Checking an entry point does not verify the pages it links to.

## Lookup routes

| Need | Entry point | Caution |
|---|---|---|
| Agent Skills format | https://agentskills.io/specification | Frontmatter fields, naming rules, size guidance |
| OOUX | https://ooux.com/what-is-ooux | Object-centred information architecture |
| ORCA | https://ooux.com/selfpacedoouxmasterclass | The compact map here is an adaptation, not full ORCA |
| GOV.UK patterns | https://design-system.service.gov.uk/patterns/ | Look up the exact question, review, and recovery patterns |
| GOV.UK releases | https://design-system.service.gov.uk/community/whats-new | Also https://github.com/alphagov/govuk-frontend/releases for the installed version |
| Carbon | https://www.carbondesignsystem.com/ | Check the supported generation. Not a mandatory visual system for data work. |
| Material 3 | https://m3.material.io/ | A readable homepage does not verify subpages |
| Compose Material 3 | https://developer.android.com/jetpack/androidx/releases/compose-material3 | Implementation release notes, not the full design specification |
| Apple HIG | https://developer.apple.com/design/human-interface-guidelines/ | Check the supported OS and SDK |
| Liquid Glass | https://developer.apple.com/documentation/technologyoverviews/liquid-glass | Version-specific changes need review |
| WCAG 2.2 | https://www.w3.org/TR/WCAG22/ | The prompts in this skill are incomplete |
| WCAG 3 status | https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/ | Working Draft, not a standard |
| ARIA APG | https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/ | Native semantics first |
| HAX | https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/ | The draft-versus-action and authorisation rules include method-authored safeguards |
| Project guidelines | The actual source supplied or found in the project | Record the exact source and version. If none, disclose the accessibility fallback. |

## Verification record

For each consequential source you rely on, record these separately:

- exact source URL
- publication date, or "not stated"
- last-update date, or "not stated"
- access date
- available version, or "not stated"
- reviewed scope: entry point, a named pattern or section, or not reviewed
- verification status for that scope, or "not verified"

Do not infer freshness from an access date. Do not treat a landing-page or entry-point check as verification of the patterns, components, or release notes it links to. If retrieval fails, continue with a reviewable proposal and name the uncertainty.

## Provenance of the 2026-10-05 snapshot

The working notes are in `references/visual-systems.md`. This review accessed sources on 2026-10-05 and does not repeat claims that were not checked.

Checked, at the scope named in the snapshot: the GOV.UK what's-new page, two Carbon MCP pages, the WCAG 2.2 Recommendation status, and the WCAG 3 introduction. Material 3 Expressive details and Apple Liquid Glass version details were not verified and were removed from the snapshot. How any specific jurisdiction treats WCAG versions in law was not verified.

## Evals

`evals/evals.json` ships test prompts. The performing agent receives only each case's `prompt`. `expected_output` and `expectations` are for the grader. Case 10 is an automatic-trigger test: do not name or invoke this method in that prompt. Presence of the file is not evidence that the cases have run. Report actual run scope and results separately, and do not imply a comparison or user-study outcome.
