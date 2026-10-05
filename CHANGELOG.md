# Changelog

## 2.2.0 — 2026-10-05

Merges the 2.1.0 purpose-based coverage with fixes from a review of that release.

- **Triggering.** Restored concrete trigger phrases to the description (wireframes, mockups, forms, dashboards, landing pages, platforms). Restored `compatibility` and `metadata.version`.
- **Skill body.** Removed the release, hash, and memory-pointer text, which now lives in the README. The body no longer asks agents to compute hashes.
- **Gate.** Replaced "signals to assess" with an explicit rule: four required conditions, three skip conditions, a three-row map when unsure, and the 2.1.0 rule that one object on screen does not justify skipping.
- **Pre-layout statement.** Capped at about five lines and limited to new visual surfaces.
- **Currency.** Restored a dated snapshot (GOV.UK Frontend v6, Carbon v11 and the v12 road, Material 3 Expressive, Liquid Glass, WCAG 2.2 and the WCAG 3 draft), with each fact marked primary or secondary and a rule to look up the installed version first.
- **Sources.** Trimmed to lookup routes, a minimal verification record, and snapshot provenance. Removed the unused GOV.UK measuring-success note and moved delegation and hash guidance to the README.
- **Evals.** Returned to the skill-creator schema (numeric `id`, `expected_output`, `expectations`), kept the seven 2.1.0 cases, and added clinic booking, SwiftUI, and portfolio cases plus a negative-trigger case (a logo request).
- **Repetition.** The system-selection table now appears once, in `SKILL.md`, with the platform defaults restored.
- **Codex metadata.** `agents/openai.yaml` now uses portable prompt wording. It remains optional.

## 2.1.0 — 2026-10-05

Added purpose-based coverage (`references/modern-design.md`), a stricter gate, a release manifest, and `agents/openai.yaml`.

## 2.0.0 — 2026-10-05

Renamed from Verso, restructured into `SKILL.md` plus references, and made agent-neutral.
