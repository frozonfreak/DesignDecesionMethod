# Visual systems and adoption

Choose a system for the supported platform, brand, and requirements. The selection rules live in `SKILL.md`. This file holds current-state lookups and adoption checks.

## Currency snapshot (accessed 2026-10-05)

These are dated lookups, not permanent defaults. Before relying on one, check the project's installed version and the exact source below. Record publication date, last-update date, and access date separately. Write "not stated" when the page does not give a field, and "not verified" when that source was not checked. A landing page or what's-new entry does not verify the patterns, components, or release notes it links to.

"Latest" in a brief means the newest stable release the project's stack supports, not the newest announcement. Prefer supported stable implementations unless an experiment is explicitly in scope.

### GOV.UK Frontend

- Exact URL: https://design-system.service.gov.uk/community/whats-new/
- Publication date: not stated for the page. The February 2026 section states that v6.0.0 updated colours to the web palette in the GOV.UK brand guidelines.
- Last-update date: the newest section on the page is August 2026. A page-level modified timestamp was not stated.
- Access date: 2026-10-05
- Available version: v6.5.0 is the newest version stated on that page (August 2026). v6.1.0 (March 2026) is an earlier 6.x release, not the newest version stated there.
- Reviewed scope: the what's-new entry point only.
- Verification status: entry point checked. Individual release notes, component patterns, and the GitHub release list were not verified.
- Build implication: read the release notes for the installed version before upgrading. Only government services use the GOV.UK look.

### Carbon

- Exact URL: https://www.carbondesignsystem.com/getting-started/carbon-mcp/prompts
- Publication date: not stated
- Last-update date: not stated
- Access date: 2026-10-05
- Available version: that page names Carbon React v11 and Carbon Web Components v11. Whether a newer major exists was not verified.
- Reviewed scope: the prompts page, plus the MCP onboarding page at https://www.carbondesignsystem.com/getting-started/carbon-mcp/onboarding-and-setup
- Verification status: those two pages checked. They document a Carbon MCP server. Component patterns, a v12 roadmap, and AI-component availability were not verified. Do not treat the v11 migration guide as proof of the current major.
- Build implication: match the installed major version. Do not adopt an unreleased major from an unverified roadmap.

### Material 3 Expressive

- Exact URL: https://m3.material.io/
- Publication date: not stated
- Last-update date: not stated
- Access date: 2026-10-05
- Available version: not verified
- Reviewed scope: not reviewed
- Verification status: not verified. Earlier claims about a May 2025 announcement, Android 16, Wear OS 6, and Compose API availability were not re-checked against the official source and are not retained.
- Build implication: opt in only where the brief or project calls for it and the installed library supports it. Keep a baseline Material 3 fallback. Confirm in the official docs before relying on a specific Expressive API.

### Apple Liquid Glass

- Exact URL: https://developer.apple.com/documentation/technologyoverviews/liquid-glass
- Publication date: not stated
- Last-update date: not stated
- Access date: 2026-10-05
- Available version: not verified
- Reviewed scope: not reviewed
- Verification status: not verified. Earlier claims about iOS 26, a version 27 refinement, and where the material sits were not re-checked against Apple's documentation and are not retained.
- Build implication: do not mandate the newest material or an OS upgrade. If a project already uses translucency, check legibility, reduced transparency, increased contrast, and an opaque fallback for the supported OS and SDK.

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
