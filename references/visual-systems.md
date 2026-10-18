# Visual systems and adoption

Choose a system for the supported platform, brand, and requirements. The selection rules live in `SKILL.md`. This file holds current-state lookups and adoption checks.

## Currency snapshot (reviewed 2026-10-18; individual access dates below)

These are dated lookups, not permanent defaults. Before relying on one, check the project's installed version and the exact source below. Record publication date, last-update date, and access date separately. Write "not stated" when the page does not give a field, and "not verified" when that source was not checked. A landing page or what's-new entry does not verify the patterns, components, or release notes it links to.

"Latest" in a brief means the newest stable release the project's stack supports, not the newest announcement. Prefer supported stable implementations unless an experiment is explicitly in scope.

### GOV.UK Frontend

- Exact URL: https://github.com/alphagov/govuk-frontend/releases/tag/v6.6.0
- Publication date: 2026-10-15
- Last-update date: not stated separately for the release notes
- Access date: 2026-10-18
- Available version: 6.6.0, released (not a prerelease)
- Reviewed scope: release notes, including the character-count change and backend-limit caution.
- Verification status: release notes checked; no component runtime or upgrade tested.
- Build implication: optional `countType` uses `Intl.Segmenter` for user-perceived characters or word boundaries. Check backend counting before enabling it and verify the unsupported-browser fallback.
- Related sources: https://design-system.service.gov.uk/community/whats-new/ (August 2026 section); https://design-system.service.gov.uk/community/component-lifecycle-statuses/; https://design-system.service.gov.uk/components/language-navigation/
- Related verification: accessed 2026-10-18; lifecycle definitions and Language navigation's Trial status checked. The August entry predates the review window; publication and last-update dates for the detailed pages are not stated. Implementation and user testing were not performed.

### Carbon

- Exact URL: https://github.com/carbon-design-system/carbon/releases/tag/v11.118.0
- Publication date: 2026-10-07
- Last-update date: not stated separately for the release notes
- Access date: 2026-10-18
- Available version: repository release 11.118.0; its React package is `@carbon/react` 1.118.0. Do not use the repository tag as an npm package version.
- Reviewed scope: release notes, especially React new features, fixes, and the separate upcoming-v12 section.
- Verification status: release notes checked; individual components and runtime behaviour not tested. This is a dated release check, not proof about every Carbon package's current major.
- Build implication: empty states and notification status icon descriptions appear among current features/fixes. Entries labelled "Upcoming in v12" do not establish released support. Match the project's actual package and version.

### Material 3 / Compose implementation

- Exact URL: https://developer.android.com/jetpack/androidx/releases/compose-material3
- Publication date: 2026-10-07 for 1.5.0-beta01
- Last-update date: release table states 2026-10-07; page-level modification date not verified
- Access date: 2026-10-18
- Available version: stable 1.4.0; prerelease 1.5.0-beta01, recorded separately from stable
- Reviewed scope: release table and 1.5.0-beta01 notes covering app-bar/slider compatibility and shape/carousel API changes.
- Verification status: Android implementation notes checked; full Material design guidance, individual Expressive API status, and web-library support not verified.
- Build implication: check the exact artifact and API before adoption. An Android beta does not establish equivalent web support or justify a project upgrade. Prefer supported stable implementations; opt into Expressive only when justified and supported.

### Apple Liquid Glass

- Exact URL: https://developer.apple.com/documentation/technologyoverviews/liquid-glass
- Publication date: not stated
- Last-update date: not stated
- Access date: 2026-10-05
- Available version: not verified
- Reviewed scope: not reviewed
- Verification status: not verified. Earlier claims about iOS 26, a version 27 refinement, and where the material sits were not re-checked against Apple's documentation and are not retained.
- Build implication: do not mandate the newest material or an OS upgrade. If a project already uses translucency, check legibility, reduced transparency, increased contrast, and an opaque fallback for the supported OS and SDK.

### Apple Widgets and Live Activities

- Exact URL: https://developer.apple.com/design/whats-new/
- Publication date: 2026-10-13 for the two announcements
- Last-update date: not stated for the page
- Access date: 2026-10-18
- Available version: not stated; these are guidance announcements, not SDK releases
- Reviewed scope: announcement entries for Widgets and Live Activities only
- Verification status: announcements checked; linked specialist guidance and specifications not reviewed
- Build implication: for those surfaces, look up the exact supported platforms, specifications, and limited-width layouts before designing. The announcement alone does not verify the requirements.

### WCAG

- Exact URL: https://www.w3.org/TR/WCAG22/
- Publication date: 12 December 2024
- Last-update date: the Recommendation date is 12 December 2024. Errata exist; the errata page was not reviewed, so later corrections are not verified.
- Access date: 2026-10-05
- Available version: WCAG 2.2, W3C Recommendation
- Reviewed scope: document status and abstract, not each success criterion
- Verification status: status checked. Success criteria were not re-verified from this page in this review.
- Related URL: https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/ — accessed 2026-10-05. WCAG 3 is an incomplete draft. The page describes September 2026 draft updates and says WCAG 3 will not supersede WCAG 2, and that WCAG 2 will not be deprecated for several years after WCAG 3 is finalized. Publication date of the introduction page: not stated. A 3 March 2026 Working Draft date was not on the page reviewed and is not verified.
- Build implication: target WCAG 2.2 AA when no stricter project requirement applies. Treat WCAG 3 as future planning only.

## Detect and preserve what exists

Inspect project tokens, components, screenshots, and installed dependencies. These signals are clues, not proof of design intent or conformance:

| Signal | Suggests |
|---|---|
| `@carbon/react`, `@carbon/styles` | Carbon v11 |
| `govuk-frontend` (note the major version) | GOV.UK Frontend |
| `androidx.compose.material3` (note the version) | Material 3 on Android |
| `@material/web`, or `--md-sys-color-*` custom properties | Material 3 on web |
| SwiftUI `glassEffect`, UIKit `UIGlassEffect` | Liquid Glass adopted |
| An in-house token file or component library | The project's own system |

A deployment target alone does not establish adoption of a visual system. Record the actual installed version and visual decisions. If the brief explicitly requests a different direction, assess that request first, including accessibility, platform constraints, and migration scope. Otherwise retain a suitable existing system. Selecting that system is separate from borrowing an interaction pattern.

Separate structural patterns from visual identity. Carbon filtering can be adapted into a Material or bespoke interface without Carbon branding. Native platform conventions can coexist with brand typography and imagery when behaviour and accessibility stay coherent. A documented bespoke system is valid, and utility CSS alone does not define one.

## Check before adopting

When adopting a component or pattern, record its exact source/library/version and upstream maturity: stable, trial, experimental, deprecated, or the source's own status. Use "not stated" or "not verified" rather than inferring stability from availability. Record why a non-stable option fits and what fallback or further validation it needs. GOV.UK currently distinguishes Trial and Stable; the broader labels here are a cross-system check, not GOV.UK's taxonomy. A stable library release does not establish every component's maturity.

When a form has character or word limits, verify that the displayed counter, accepted input, backend validation, and error message agree on the counting unit and locale. Check supported languages (for example Tamil and English), combining marks, emoji, limit boundaries, and browser/no-JavaScript fallbacks where relevant. If the backend is unavailable, mark consistency unverified and propose boundary tests; do not claim that visual inspection proves it. This check applies to text limits, not every UI change.

- **Material 3.** Specific guidance, installed implementation support, tokens, and behaviour. Expressive options only where justified.
- **Apple HIG.** Supported OS and SDK, the existing design, whether the material suits the content, and accessibility preferences.
- **GOV.UK.** Service branding requirements and the installed Frontend version.
- **Carbon.** The installed generation, actual tokens and components, density needs, and migration constraints.
- **Bespoke or editorial.** Role-based typography, semantic colours, composition, media, and consistent behaviour.

## Relevant foundations before layout

State or verify colour roles, typography, meaningful component states, focus, error text, and disabled and read-only behaviour. Decide shape, elevation, navigation, adaptive layout, and motion when relevant. Reuse exact established project roles instead of redesigning them. If upstream verification is unavailable, label it and still define a reviewable proposed choice.

## Expression and materials

Material Expressive and Apple Liquid Glass are options within applicable platform guidance, not universal definitions of modern design. Use emphasis sparingly, according to the hierarchy and purpose of the screen. Restrained and expressive designs are both valid when they serve that purpose. Do not apply a quota for key moments or for trends such as gradients, glass, or oversized type.

For translucent controls, assess legibility over worst-case content, the reduced-transparency and increased-contrast settings, and a supported opaque fallback. Keep navigation and content layers distinguishable according to the platform's guidance. Do not mimic platform materials for novelty, and do not mandate an OS upgrade or migration as part of an unrelated UI task.

## Preferences and transitions

Respect reduced motion, text scaling, increased contrast, forced colours, and transparency settings. Include light and dark themes when supported or required, and do not invent them otherwise. Resolve visual-system changes deliberately: record affected components, compatibility adapters, and validation. Avoid silently mixing incompatible tokens or generations.
