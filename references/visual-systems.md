# Visual systems and adoption

Choose a system for the supported platform, brand, and requirements. The selection rules live in `SKILL.md`. This file holds current-state lookups and adoption checks.

## Currency snapshot (checked 2026-10-05)

These are dated lookups, not permanent defaults. Before relying on one, check the project's installed version and the official release notes. If you cannot browse, say the fact is unverified as of the snapshot date. "Secondary" means a third-party report, so confirm it against the publisher before depending on it.

| System | Snapshot | Source type | Build implication |
|---|---|---|---|
| GOV.UK Frontend | v6.0.0 (Feb 2026) applied the refreshed brand colour palette, and v6.1.0 followed in Mar 2026. Newer 6.x releases may exist. | Primary (GOV.UK Design System site) | Read the release notes before moving from v5 to v6. Only government services use the GOV.UK look. |
| Carbon | v11 is the current major version. "Carbon Next" outlines the road to v12, which is not released. Carbon also ships AI components and an MCP server. | Primary (Carbon site) | Match the installed major version. Do not build against v12 material yet. |
| Material 3 Expressive | Announced May 2025 as an evolution of Material 3, not a "Material 4". Adds spring-based motion, richer colour, new shapes, emphasised type, and new components. Reached Android 16 and Wear OS 6 first. A community note (Aug 2026) reports that some Compose Expressive APIs needed newer or alpha library builds. | Secondary | Opt-in. Confirm in the official docs and the installed library, and keep a baseline Material 3 fallback. |
| Apple Liquid Glass | Introduced at WWDC 2025 with the iOS 26 releases, and reported as refined for the version 27 releases at WWDC 2026. Apple's guidance is reported to place it in the navigation and controls layer, above content. | Primary for existence and adoption guidance (Apple developer docs). Secondary for version 27 details. | System components adopt it automatically. Custom controls need their own legibility and reduced-transparency handling. |
| WCAG | WCAG 2.2 is the current Recommendation. WCAG 3.0 is a Working Draft (3 Mar 2026) and does not deprecate WCAG 2. | Primary (W3C) | Target WCAG 2.2 AA. Treat WCAG 3 as future planning only. |

"Latest" in a brief means the newest stable release the project's stack supports, not the newest announcement. Prefer supported stable implementations unless an experiment is explicitly in scope.

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

A deployment target alone does not establish adoption of a visual system. Record the actual installed version and visual decisions, and retain a suitable existing system unless the brief authorises changing it.

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

Material Expressive and Apple Liquid Glass are options within applicable platform guidance, not universal definitions of modern design. Use emphasis and motion only when they help the experience, and reserve strong emphasis for one or two key moments per screen.

For translucent controls, assess legibility over worst-case content, the reduced-transparency and increased-contrast settings, and a supported opaque fallback. Keep navigation and content layers distinguishable according to the platform's guidance. Do not mimic platform materials for novelty, and do not mandate an OS upgrade or migration as part of an unrelated UI task.

## Preferences and transitions

Respect reduced motion, text scaling, increased contrast, forced colours, and transparency settings. Include light and dark themes when supported or required, and do not invent them otherwise. Resolve visual-system changes deliberately: record affected components, compatibility adapters, and validation. Avoid silently mixing incompatible tokens or generations.
