# Changelog

## 2.2.2 — 2026-10-05

Explains the method for people opening the repository. The procedure is unchanged.

- **Introduction.** States what the workflow is, the repeated guesswork it addresses, and why this team keeps it: a shared philosophy across products and agents. Time savings remain unmeasured.
- **WebHIG.** Records the separate responsibilities. This method decides the experience; WebHIG defines applicable interface quality requirements.

## 2.2.1 — 2026-10-05

Bounded corrections to selection order, object-map scope, presentation scope, source freshness, visual emphasis, and evaluation expectations.

- **Selection.** An explicit request for a different direction is assessed before an existing system is retained. System selection stays distinct from borrowing an interaction pattern.
- **Object map.** A produced or verified map is required when relationships affect the navigation, routes, or screen structure being changed. The four conditions are signals scoped to that change. Reuse a verified map. Use the smallest sufficient map instead of a fixed three-row fallback. The gate remains before layout.
- **Presentation.** The compact direction statement covers consequential changes to purpose, hierarchy, composition, density, or responsive behaviour, including existing themed screens. It stays brief, and it is skipped when those decisions do not change.
- **Freshness.** Source records keep publication, last-update, and access dates separate, with the exact URL, available version, reviewed scope, and verification status. Unchecked snapshot claims were removed rather than repeated.
- **Emphasis.** Use emphasis sparingly according to hierarchy and purpose. There is no quota for key moments.
- **Evals.** Clinic filtering is conditional on filtering being added. SwiftUI accepts suitable system controls without requiring glass. Portfolio mapping is judged by structural relevance. The logo case is an automatic-trigger test, and grader expectations stay out of the task prompt.
- **History.** The supplied 2.1.0 release contained six evaluation cases, not seven.

## 2.2.0 — 2026-10-05

Merges the 2.1.0 purpose-based coverage with fixes from a review of that release.

- **Triggering.** Restored concrete trigger phrases to the description (wireframes, mockups, forms, dashboards, landing pages, platforms). Restored `compatibility` and `metadata.version`.
- **Skill body.** Removed the release, hash, and memory-pointer text, which now lives in the README. The body no longer asks agents to compute hashes.
- **Gate.** Replaced "signals to assess" with an explicit rule: four required conditions, three skip conditions, a three-row map when unsure, and the 2.1.0 rule that one object on screen does not justify skipping.
- **Pre-layout statement.** Capped at about five lines and limited to new visual surfaces.
- **Currency.** Restored a dated snapshot (GOV.UK Frontend v6, Carbon v11 and the v12 road, Material 3 Expressive, Liquid Glass, WCAG 2.2 and the WCAG 3 draft), with each fact marked primary or secondary and a rule to look up the installed version first.
- **Sources.** Trimmed to lookup routes, a minimal verification record, and snapshot provenance. Removed the unused GOV.UK measuring-success note and moved delegation and hash guidance to the README.
- **Evals.** Returned to the skill-creator schema (numeric `id`, `expected_output`, `expectations`), kept the six 2.1.0 cases, and added clinic booking, SwiftUI, and portfolio cases plus a negative-trigger case (a logo request).
- **Repetition.** The system-selection table now appears once, in `SKILL.md`, with the platform defaults restored.
- **Codex metadata.** `agents/openai.yaml` now uses portable prompt wording. It remains optional.

## 2.1.0 — 2026-10-05

Added purpose-based coverage (`references/modern-design.md`), a stricter gate, a release manifest, and `agents/openai.yaml`.

## 2.0.0 — 2026-10-05

Renamed from Verso, restructured into `SKILL.md` plus references, and made agent-neutral.
