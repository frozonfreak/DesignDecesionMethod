# Routing: which guidance for which problem

These are recommendations from this skill, not exclusive capabilities of the upstream sources. Use them per problem, flow, or screen. There is no ranking, and no source is mandatory.

## Matrix

| Need | Start with | Take from it | Avoid |
|---|---|---|---|
| Connected entities, unclear navigation | OOUX / ORCA | Recognisable objects, relationships, attributes, actions, contextual routes | Mirroring every database entity, exposing internal complexity, mocking up screens before the object map |
| Unfamiliar, occasional, or consequential task | GOV.UK | Plain explanation, relevant questions, sensible sequence, review, confirmation, recovery | Extra steps for routine expert entry, forced one-question pages for frequent work, government branding |
| Frequent, data-heavy work | Carbon | Search and filter strategy, selection, bulk actions, forms, system feedback | Defaulting to dense tables regardless of audience |
| Native look and behaviour on Apple platforms | Apple HIG | Navigation, controls and conventions appropriate to the supported platform/version | Mimicking the material on other platforms |
| Consistent appearance on Android or web with no existing system | Material 3 | Colour roles, type, shape, components, states, adaptive layout | Ad hoc styling, mixing systems |
| Interaction quality in a specific product | The project's own guidelines (for example a project Web HIG) | Accessibility, behaviour, responsiveness, performance | Inventing a version, requirements, or compliance |
| Any AI or agent feature | `ai-interfaces.md` | Capability clarity, provenance, correction, authorised actions | Adding AI controls to non-AI products |

## Context changes the choice

- **Portfolio or marketing site.** Clarify the visitor's questions and routes with content-first guidance. Map objects only if projects or services relate to each other. Do not invent an operational dashboard.
- **Routine data entry** (daily logs, harvest records, check-ins). Connect the entered record to the objects it belongs to using the object map. Prefer one short form if it is efficient. Borrow GOV.UK wording and recovery, and Carbon form states.
- **Operations or campaign tooling.** Map the product, campaign, and channel relationships. Use Carbon-style data patterns. Use guided content for first-time connection and for review before anything is sent.
- **Unfamiliar application.** Use a clear sequence and a confirmation step. Establish object relationships only as far as navigation needs them. Avoid premature bulk controls.
- **Native mobile screen.** Use the platform's guidance for navigation and controls. Use the object map only to decide what each tab or destination represents.

## Reuse a pattern when the task and context match, not because its screenshot looks good

Check the guidance for the specific pattern before implementing it. Styling must keep the semantic structure, validation, focus, and accessible behaviour.

## Adaptation line example

> GOV.UK rule: one question per page. This design: one form of five fields. Why: daily expert entry, low error cost, repeated many times a day, so the extra pages cost more than they protect.

## Effort comparison

For a materially different task pattern, record frequency, familiarity, cost of error, device, the pattern chosen, and why. Compare likely reading, recall, entry, navigation, and recovery effort. Treat this as a heuristic, not measured effort.

## Broader purposes and extensions

Use `modern-design.md` for editorial, discovery, commerce, creative and collaborative experiences and specialist requirements. The core owns the conditional object-map gate; examples here cannot override it. Select only guidance that resolves a real problem. Use actual project HIG where supplied; if unavailable, disclose that gap and use the accessibility fallback. Performance budgets and other HIG-specific requirements remain project-defined or unspecified; WCAG/APG do not replace them.
