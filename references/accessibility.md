# Accessibility baseline and verification

## Target

- Web: WCAG 2.2 AA when the project supplies no standard. A stronger project or legal requirement wins. Flag conflicts instead of silently lowering the bar.
- Native apps: the platform's accessibility guidance and tools. Do not claim web checks validate native accessibility.
- This is a design and verification target, not a compliance claim. Confirm which WCAG version a jurisdiction's law references, because many regimes cite WCAG 2.x.
- WCAG 3.0 is a Working Draft and does not replace WCAG 2.2 yet. Do not design to it.

## Checks (prompts, not the complete standard)

- **Keyboard and focus.** Everything operable by keyboard, logical order, visible focus, and the focused control not hidden behind sticky bars or overlays.
- **Names, roles, states.** Labels, accessible names, error text associated with its field, and announcements for meaningful status changes.
- **Contrast and scaling.** Text and non-text contrast, zoom and reflow, text resizing, and no meaning carried by colour alone.
- **Targets.** Pointer targets meet the applicable size and spacing rules, with a drag alternative. WCAG's minimum is not an ideal touch size, so follow the platform's larger recommended sizes where they apply.
- **Repeated effort.** Consistent help where repeated, no redundant re-entry of data, and accessible authentication including password-manager and paste support.
- **Motion.** Reduced-motion preference respected, and nothing essential depends on animation.

## User preferences to honour

Reduced motion, reduced transparency, increased contrast, forced colours, dark mode, and text scaling (including Dynamic Type on Apple platforms). Translucent glass and expressive visuals need contrast verified against the worst-case background, not the average one.

## Verification

Combine automated checks with manual keyboard testing and relevant assistive-technology pairs. For native apps use that platform's inspection tools. Record what was not tested and whether project guidelines were available. Distinguish heuristic review, automated checks, manual testing, and user research.
