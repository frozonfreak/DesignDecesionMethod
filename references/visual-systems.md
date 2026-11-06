# Visual systems and adoption

Choose a system for the supported platform, brand, and requirements. The selection rules live in `SKILL.md`. This file holds current-state lookups and adoption checks.

## Currency snapshot (reviewed 2026-11-06; individual access dates below)

These are dated lookups, not permanent defaults. Before relying on one, check the project's installed version and the exact source below. Record publication date, last-update date, and access date separately. Write "not stated" when the page does not give a field, and "not verified" when that source was not checked. A landing page or what's-new entry does not verify the patterns, components, or release notes it links to.

"Latest" in a brief means the newest stable release the project's stack supports, not the newest announcement. Prefer supported stable implementations unless an experiment is explicitly in scope.

### GOV.UK Frontend

- Exact URL: https://github.com/alphagov/govuk-frontend/releases/tag/v6.6.0
- Publication date: 2026-10-15
- Last-update date: not stated separately for the release notes
- Access date: 2026-11-06
- Available version: 6.6.0, released (not a prerelease). The published releases list has no newer tag.
- Reviewed scope: release identity. The 6.6.0 notes, including the character-count change and backend-limit caution, were checked on 2026-10-18 and were not re-read line by line in this window.
- Verification status: release list checked; no component runtime or upgrade tested.
- Build implication: optional `countType` uses `Intl.Segmenter` for user-perceived characters or word boundaries. Check backend counting before enabling it and verify the unsupported-browser fallback.
- Related sources: https://design-system.service.gov.uk/community/whats-new/; https://design-system.service.gov.uk/community/component-lifecycle-statuses/; https://design-system.service.gov.uk/components/language-navigation/
- Related verification: Language navigation was opened on 2026-11-06 and is still marked Trial. Its recent-changes table says the component was introduced in August 2026 with Frontend 6.5.0. A check of the what's-new page showed October 2026, for Frontend 6.6.0, as the newest dated section. Lifecycle definitions were not re-opened. Publication and last-update dates for those pages are not stated. Implementation and user testing were not performed.

### Carbon

- Exact URL: https://github.com/carbon-design-system/carbon/releases/tag/v11.120.0
- Publication date: 2026-11-04
- Last-update date: not stated separately for the release notes
- Access date: 2026-11-06
- Available version: repository release 11.120.0; its React package is `@carbon/react` 1.120.0. The intervening stable release 11.119.0 was published 2026-10-21, with `@carbon/react` 1.119.0. Do not use the repository tag as an npm package version.
- Reviewed scope: release notes for 11.119.0 and 11.120.0, especially React features, fixes, and sections labelled upcoming in v12. The release-schedule status table at tag v11.120.0 was also checked: https://github.com/carbon-design-system/carbon/blob/v11.120.0/docs/release-schedule.md
- Verification status: release notes and that status table checked; individual components and runtime behaviour not tested. This is a dated release check, not proof about every Carbon package's current major.
- Build implication: the schedule table marks v11 active and v12 preview. Entries labelled "Upcoming in v12" do not establish released support. Current-line notes include side-nav button items and a number-input extra-small size in 11.119.0, and DataTable sticky-header support in 11.120.0, plus accessibility fixes. The 11.118.0 notes previously recorded empty states and notification status icon descriptions; those notes were not re-reviewed here. Match the project's actual package and version.

### Material 3 / Compose implementation

- Exact URL: https://developer.android.com/jetpack/androidx/releases/compose-material3
- Publication date: 2026-11-04 for 1.5.0-rc01. The same page dates stable 1.4.0 at 2025-09-24.
- Last-update date: the release table states 2026-11-04; page-level modification date not verified
- Access date: 2026-11-06
- Available version: stable 1.4.0; release candidate 1.5.0-rc01, recorded separately from stable. Intermediate 1.5.0-beta02, published 2026-10-21, lists no change notes on this page. The 1.5.0-beta01 shape and carousel API notes remain on the page.
- Reviewed scope: release table, 1.5.0-rc01 notes, the 1.5.0-beta02 heading, and the still-listed 1.5.0-beta01 API notes. The official web library page was checked separately: https://m3.material.io/develop/web
- Verification status: Android release notes and the web library announcement checked. Individual Expressive APIs, web component behaviour, and a publication date for the web page were not verified. The web page does not state a last-update date.
- Build implication: 1.5.0-rc01 notes cover a ToggleButton pressed-shape token and Slider and RangeSlider fixes. They do not replace stable 1.4.0. The web library page says Material Web Components are in maintenance mode and Material 3 Expressive is not implemented on Web. An Android release candidate does not establish web support or justify a project upgrade. Prefer a supported stable implementation; opt into Expressive only where the brief calls for it and the installed library supports it.

### Apple Liquid Glass

- Exact URL: https://developer.apple.com/documentation/technologyoverviews/liquid-glass
- Publication date: not stated
- Last-update date: the HTTP Last-Modified header was 2026-11-05. That is a transport timestamp, not a documentation revision stated in the page.
- Access date: 2026-11-06
- Available version: not verified
- Reviewed scope: HTML shell only. The title and a short meta description were present. The guidance body is loaded by script and was not reviewed.
- Verification status: not verified. Earlier claims about iOS 26, a version 27 refinement, and where the material sits were not checked against the rendered documentation and are not retained.
- Build implication: do not mandate the newest material or an OS upgrade. If a project already uses translucency, check legibility, reduced transparency, increased contrast, and an opaque fallback for the supported OS and SDK.

### Apple Widgets and Live Activities

- Exact URL: https://developer.apple.com/design/whats-new/
- Publication date: 2026-10-13 for the two announcements
- Last-update date: not stated for the page
- Access date: 2026-11-06
- Available version: not stated; these are guidance announcements, not SDK releases
- Reviewed scope: announcement entries for Widgets and Live Activities only. Both entries are still listed.
- Verification status: announcements checked; linked specialist guidance and specifications not reviewed
- Build implication: for those surfaces, look up the exact supported platforms, specifications, and limited-width layouts before designing. The announcement alone does not verify the requirements.

### Apple design updates, 28 October 2026

- Exact URL: https://developer.apple.com/design/whats-new/
- Publication date: 2026-10-28 for the four announcements
- Last-update date: not stated for the page
- Access date: 2026-11-06
- Available version: not stated; these are guidance announcements, not SDK releases
- Reviewed scope: announcement entries for Designing for macOS, Gestures, Pointing devices, and App icons
- Verification status: announcements checked; linked specialist guidance and specifications not reviewed
- Build implication: macOS touch input, gestures, pointing-device behaviour, and app-icon format options need the linked Human Interface Guidelines for the supported OS and SDK. The announcement alone does not verify those requirements. Do not mandate a macOS upgrade for an unrelated interface.

### WCAG

- Exact URL: https://www.w3.org/TR/WCAG22/
- Publication date: 12 December 2024
- Last-update date: the Recommendation date is 12 December 2024. The status section says errata exist. The errata page was not reviewed, so later corrections are not verified.
- Access date: 2026-11-06
- Available version: WCAG 2.2, W3C Recommendation
- Reviewed scope: document status and abstract, not each success criterion
- Verification status: status checked. Success criteria were not re-verified from this page in this review.
- Related URL: https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/ — accessed 2026-11-06. The introduction page states "Updated: 25 September 2026." WCAG 3 remains an incomplete draft. The page describes September 2026 draft updates and says WCAG 3 will not supersede WCAG 2, and that WCAG 2 will not be deprecated for several years after WCAG 3 is finalized. A Working Draft date for the guidelines document was not on the introduction page reviewed.
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
