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

For each consequential source you rely on, record the URL, the version if stated, the date accessed, and the reviewed scope: entry point checked, specific guidance reviewed, or unverified. Write "not stated" for anything missing, and never infer freshness from an access date. If retrieval fails, continue with a reviewable proposal and name the uncertainty.

## Provenance of the 2026-10-05 snapshot

Primary pages read: the GOV.UK Design System site and its what's-new page, the Carbon site, the W3C WCAG 3 draft and news page, the Apple Liquid Glass documentation page, and the Agent Skills specification.

Secondary reports used, to be confirmed against the publisher: a news report on the Material 3 Expressive announcement, a community note on Compose Expressive API availability, and third-party summaries of the version 27 Liquid Glass refinements.

Not verified: the exact Liquid Glass changes in the version 27 releases, which GOV.UK Frontend 6.x release is newest today, and how any specific jurisdiction treats WCAG versions in law.

## Evals

`evals/evals.json` ships test prompts. Their presence is not evidence that they have run. Report actual run scope and results separately, and do not imply a comparison or user-study outcome.
