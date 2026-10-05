---
name: design-decision-method
description: >-
  Decide and record design choices before building any UI. Use whenever a task involves designing, reviewing, or implementing screens, flows, forms, navigation, dashboards, landing pages, wireframes, mockups, prototypes, or UI copy for web, Android, iOS, or cross-platform products (operational, editorial, exploratory, commerce, creative, collaborative, or AI-enabled), even if the user never mentions design methods. Routes work across OOUX/ORCA object mapping, GOV.UK, Carbon, Material 3, platform guidance such as Apple's HIG, and the project's own guidelines; requires an object map and decision record before layout when relationships shape structure; checks accessibility against WCAG 2.2 AA. Not for standalone logo, icon, or social-image generation, or for inventing a new visual system.
compatibility: Any agent that supports the Agent Skills format (SKILL.md). No network access or special tools required; writing files is optional and has an inline fallback.
metadata:
  version: "2.2.1"
  updated: "2026-10-05"
  formerly: "verso"
---

# Design Decision Method

Make design decisions explicit before drawing or coding the screen. This skill routes a UI task to established guidance (OOUX, GOV.UK, Carbon, Material 3, platform guidelines, the project's own rules), requires a short object map and decision record when they would change the structure, and ends with an honest statement of what was and was not verified. It does not invent a visual system, rank the sources, or borrow their branding.

This method owns project-specific decisions and their rationale. The project's guidelines own applicable quality requirements, a design system owns visual and component conventions, and a UI library implements them. Tailwind is implementation tooling, not a design system. This is not an exhaustive pattern library or proof of production readiness.

Read the reference modules listed under "Read next" when their condition applies. If you cannot open them, say so and mark the affected checks as unverified instead of claiming them.

## Workflow

### 1. Establish context

Read the brief, the existing product (code, tokens, components, screenshots) and any project guidelines before deciding anything. Identify audience and roles, familiarity, primary tasks and how often they happen, the cost of error, device and input, language, connectivity, brand, constraints, and success criteria.

Identify the experience purpose: operational work, reading and storytelling, exploration, evaluation and purchase, creation and editing, or participation and collaboration. Mixed-purpose products can use a different approach per flow. Read `references/modern-design.md` for purpose-based presentation and specialist requirements.

Separate what you know from what you assume. Do not invent business rules, authorisation requirements, or product capabilities, and label optional additions. Ask the user only about gaps that would materially change the design, and keep working on everything else. If you cannot ask, list the assumptions in the deliverable. Do not import one domain's conventions into another (for example, an operations dashboard for a portfolio site).

### 2. Choose the visual system

Use the first row that applies:

| Situation | Decision |
|---|---|
| The brief explicitly requests a different direction | Honour that request. Identify accessibility and platform constraints and the migration scope, and record consequential conflicts. |
| A suitable existing system, brand, or platform direction | Retain and extend it. Verify its actual tokens, components, and supported versions. |
| Native Apple interface (iOS, iPadOS, macOS, visionOS), no existing system | Apple HIG and system controls for the supported OS and SDK. Do not mandate the newest material or an OS upgrade. |
| Android or Compose, no existing system | Material 3. Use Expressive only where the brief or project calls for it and the installed library supports it. |
| UK government service | GOV.UK Design System at the installed Frontend version. |
| A documented bespoke or editorial brand direction | Define coherent, reusable, role-based visual decisions. Keep familiar, accessible behaviour. |
| Other web or cross-platform work with no system | Material 3 as the fallback, with implementation support checked. |

Choosing a visual system is separate from borrowing an interaction pattern. Borrow GOV.UK and Carbon patterns when they solve the task. Workload alone does not require adopting their visual identity, and GOV.UK branding is for government services only. Do not mix competing visual identities, or generations of one system, on one surface. A deliberate adapter or staged migration needs explicit consistency and behaviour checks.

Read `references/visual-systems.md` for current versions and adoption checks.

**Presentation direction.** When a change affects purpose, hierarchy, composition, density, or responsive behaviour, write a compact direction statement: the experience purpose, what must be understood first, composition and density, imagery or motion if any, and device adaptation. This includes an existing themed screen when those decisions change. Keep it brief and proportional to the change, and omit dimensions that do not apply. Skip it when the change does not affect those decisions. Reading or exploration need not end in a transaction or a single primary button.

### 3. Object map (gate before layout)

Produce or reuse a verified map before wireframes, mockups, or code when meaningful relationships affect the navigation, routes, or screen structure being designed or changed. Existing product complexity alone does not require a map for an unrelated copy or styling fix.

Treat these as structural signals, scoped to the requested change:

- two or more object types that people move between in that change;
- an object reachable from more than one place in the structure being designed or changed;
- top-level navigation that is new or changing;
- a form or screen that creates or edits a record relating to objects elsewhere in the product, when that relationship affects the structure being changed.

One object on screen does not by itself justify skipping when one of these signals applies to the change. Skip the map when none of them apply, including a copy-only fix, a purely visual restyle, or a component-level fix with unchanged structure.

Map user-recognisable objects, relationships, decision-relevant attributes, and actions, from the user's mental model rather than the database schema. Use the smallest map that is sufficient for the change. Derive screens and routes from the map instead of backfilling it after layout. Reuse a verified existing map and record what changed. This is a lightweight adaptation, not a claim of completing the full ORCA method.

Record `Map: produced / reused / skipped — <reason>` in one line. Use `assets/design-record-template.md`. Save it as `docs/design/<slug>.md` when the project's conventions and scope support a saved record, and otherwise deliver a compact inline record. The template is a scaffold, not mandatory overhead.

### 4. Decision record

For each consequential pattern choice, record task frequency, user familiarity, cost of error, and device, then the pattern chosen and why. Compare reading, recall, entry, navigation, and recovery effort rather than counting clicks or visible elements. Cite a source only when it resolves an actual design problem.

When the design departs from a cited source's rule, add one adaptation line: source rule / what this design does instead / why the frequency, familiarity, or error cost requires it. Never present an adaptation as upstream guidance.

For a new visual surface, state the colour roles, type scale, shape, motion, focus style, error text, and disabled or read-only behaviour, or name the verified project tokens and components being inherited. Inheriting a theme does not verify new focus, error, disabled, read-only, or asynchronous behaviour, so record unverified items explicitly. Scale all of this to scope: a small change gets a few lines.

### 5. Structure each view

For each important view define its purpose, orientation, decision-critical information, relevant actions, secondary content, and supporting detail.

- Show context, status, and next actions early. Keep comparisons, consequences, warnings, and recovery visible at the point of decision.
- Group by user concepts and tasks. Keep names consistent, and give numbers units, periods, and comparisons.
- Reveal optional complexity progressively. Choose formats by need: tables to compare, lists to scan, charts for trends, forms to enter data.
- Cover loading, empty, partial, error, read-only, success, permission, and offline states where they apply. Do not invent offline capability the product lacks.
- Adapt to the device without silently removing essential capabilities.

### 6. Deliver and validate

Deliver the requested artifact (spec, mockup, prototype, or code), the consequential decisions and assumptions, and a short validation status. Keep framework names out of end-user flows and UI copy.

Define a few observable acceptance criteria matched to the experience purpose (comprehension, discovery, informed purchase, creative control, or task execution) before validating, and label each result by its evidence level: proposed, heuristic review, automated check, manual test, or user research. A mockup can show routes and states but cannot establish task-completion rates. Read `references/acceptance-and-validation.md` for the record format.

For reviews, label each finding keep, change, or defer, and present speculative additions as optional. Record the versions you relied on: this skill (see `metadata.version`), the design system, and the project guidelines, or "none supplied".

## Priorities when guidance conflicts

Resolve conflicts from the project context, not from a fixed ranking of frameworks:

1. Explicit requirements, applicable accessibility obligations, and the cost of error. Flag conflicts instead of quietly lowering accessibility.
2. Comprehension, decision-critical information, and task completion.
3. Effort fitted to task frequency, familiarity, device, and context.
4. Visual consistency and appropriate brand expression.

Choose the least complex solution that is adequate.

## Rules that protect the user

- Keep essential information and recovery visible. Do not remove content for whitespace, or add decorative metrics and cards without purpose.
- Do not fabricate measurements, research, citations, confidence figures, or compliance claims. Say "not tested" instead.
- Do not add AI controls to a product that has no AI feature.
- Do not copy another organisation's branding or imply that its authors endorse a combined workflow.
- Use native semantics first and ARIA only where needed. Rebuild patterns in the target stack, preserving meaning, behaviour, focus, and feedback instead of copying upstream markup.

## Read next

| When | Read |
|---|---|
| Establishing experience purpose, composition, or specialist requirements | `references/modern-design.md` |
| Choosing between guidance sources, or unsure which pattern fits | `references/routing.md` |
| Choosing or adopting a visual system or version | `references/visual-systems.md` |
| Any UI that will be built or reviewed | `references/accessibility.md` |
| The feature involves AI, generation, suggestions, or automated actions | `references/ai-interfaces.md` |
| Defining acceptance criteria or reporting validation | `references/acceptance-and-validation.md` |
| Before citing a source or claiming something was checked | `references/sources.md` |
