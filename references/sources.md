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
| Carbon releases | https://github.com/carbon-design-system/carbon/releases | Match the exact package version; upcoming sections do not establish availability. |
| GOV.UK lifecycle | https://design-system.service.gov.uk/community/component-lifecycle-statuses/ | Check the named component as well as the lifecycle definitions. |
| Apple design updates | https://developer.apple.com/design/whats-new/ | Announcements route specialist lookup; they do not verify linked requirements. |
| Agent post-task review research | https://arxiv.org/abs/2609.13136 | Research evidence; DDM adaptations are not universal requirements. |
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
- available version, stable/prerelease channel, and component maturity when adopting a pattern; use "not stated" or "not verified" as appropriate
- reviewed scope: entry point, a named pattern or section, or not reviewed
- verification status for that scope, or "not verified"

Do not infer freshness from an access date. Do not treat a landing-page or entry-point check as verification of the patterns, components, or release notes it links to. If retrieval fails, continue with a reviewable proposal and name the uncertainty.

## Provenance of the 2026-10-18 refresh

The dated records are in `references/visual-systems.md`. The upstream-change window is 6–18 October 2026, following the 2.2.4 baseline at commit 6bab8b5. The refresh preserves the MIT license and WebHIG explanation from that baseline.

Accessed on 2026-10-18: GOV.UK Frontend 6.6.0 release notes; Carbon 11.118.0 release notes; Compose Material 3's release table and 1.5.0-beta01 notes; Apple's 13 October Widgets and Live Activities announcements. No implementation was exercised. Apple's detailed guidance remains unverified.

Older material checked on 2026-10-18: GOV.UK's August entry, lifecycle definitions, and Language navigation Trial status; the Trace2Flow abstract and submission metadata at https://arxiv.org/abs/2609.13136. The paper was submitted 2026-09-11; no separate last-update date was stated. The abstract reports a 20-participant study comparing post-task workflows with a prompt-only condition. Full methods and results were not reviewed. The conditional action-review check is DDM's adaptation, with no requirement to use a graph and no claim of DDM effectiveness.

The WCAG and Liquid Glass records retain their 2026-10-05 access dates and verification limits; they were not re-reviewed here. Legal applicability was not verified. WCAG 2.2 AA remains the default web baseline.

## Provenance of the 2026-11-06 refresh

The dated records are in `references/visual-systems.md`. The upstream-change window is 19 October–6 November 2026, following the 2.4.0 release. The six-step method, object-map gate, system-selection order, ULPG integration revision, and WCAG 2.2 AA default are unchanged. No implementation was exercised.

Accessed on 2026-11-06: the GOV.UK Frontend releases list, still 6.6.0, and the Language navigation page, still Trial; Carbon 11.119.0 and 11.120.0 release notes and the release-schedule status table at tag v11.120.0 (v11 active, v12 preview); the Compose Material 3 release table, with stable 1.4.0 and release candidate 1.5.0-rc01; the official Material Web page, which says the library is in maintenance and Expressive is not implemented on Web; Apple's what's-new page, including the 28 October announcements and the still-listed 13 October Widgets and Live Activities entries; the WCAG 2.2 recommendation status; the WCAG 3 introduction. The Liquid Glass URL returned an HTML shell whose guidance body was not reviewed. The Trace2Flow abstract page still shows only version 1, submitted 2026-09-11. Full methods and results were not reviewed.

Not opened in this window: HAX, ARIA APG, OOUX, ORCA, Apple's linked specialist pages, the WCAG 2.2 errata page, and the ULPG source files. ULPG `main` remains `a42a2faa0b097639f96e4a3e9c3d399084ebadcf`. WebHIG tag v1.16.0 exists, dated 2026-11-04, with the tag message "Release v1.16.0: field metrics and scroll-driven motion." Those requirements were not opened or copied. The 2026-10-05 project-page decision records still name Web HIG Quick Reference v1.12.5 because that was the version used then. Legal applicability was not verified.

Cursor skill directories were checked against https://cursor.com/docs/skills on 2026-11-06. The recorded project and user paths still match. Claude Code, Gemini CLI, Codex, and Claude.ai paths were not re-opened.

## Evals

`evals/evals.json` ships test prompts. The performing agent receives only each case's `prompt`. `expected_output` and `expectations` are for the grader. Case 10 is an automatic-trigger test: do not name or invoke this method in that prompt. Presence of the file is not evidence that the cases have run. Report actual run scope and results separately, and do not imply a comparison or user-study outcome.
