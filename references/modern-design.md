# Modern design selection and extension

Use these method-authored heuristics to choose presentation from requirements. They are not upstream standards, mandatory screen templates, or demographic rules. Mixed-purpose experiences can use several rows; do not force equal coverage.

## Select by experience purpose

| Purpose | Information and interaction priorities | Appropriate expression | Acceptance examples |
|---|---|---|---|
| Operational work | Stable placement, relevant density, fast entry, visible state, reversible actions and comparison | Restrained or balanced; emphasize exception and action hierarchy | Complete representative work; retain context and recover from errors |
| Reading and storytelling | Reading order, headings, pacing, credible evidence, meaningful media and routes into deeper content | Editorial typography, varied composition and imagery when useful | Understand the message; locate evidence; read comfortably on target devices |
| Discovery and exploration | Browse/search, relevant facets, relationships, comparison, clear location and a route back | Content-led grids, lists, maps or charts according to information | Find a relevant item; compare alternatives; preserve exploration context |
| Commerce and evaluation | Suitability, variations, availability, total cost, delivery/terms, evidence and informed commitment | Brand expression with legible transactional information | Make an informed choice; understand cost and outcome; correct the order |
| Creation and editing | Direct manipulation, tools near work, undo, versions, autosave status, shortcuts and uninterrupted attention | Workspace composition; density adapts to proficiency and input | Make and revise work; preserve edits; recover a previous state |
| Participation and collaboration | Roles, audience/visibility, contribution context, concurrent changes and permission feedback | Content/community appropriate; avoid unsupported social mechanics | Know who can see/change content; contribute and resolve conflicts |

Treat landing pages and portfolios as communication and evaluation experiences; do not assume a dashboard. Treat AI as a capability within a purpose, not a reason to replace every interface with chat. Apply AI-specific safeguards only where needed.

## Define the presentation before layout

When a change affects purpose, hierarchy, composition, density, or responsive behaviour, record a compact direction statement, including on an existing themed screen. Skip it when the change does not affect those decisions. Keep it brief and proportional. Do not demand a second long document.

- **Content hierarchy:** Identify what must be understood first, what supports a decision, and what can be disclosed later. A reading experience may prioritize narrative; an operator may prioritize the current object and its state.
- **Composition and density:** Choose structure from content and tasks. Consider editorial sections, split views, master/detail, canvases, comparison tables or focused flows. Neither minimalism nor density is a universal objective. Whitespace must support grouping and reading rather than conceal necessary information.
- **Typography:** Reuse the selected system's scale or define a coherent role-based scale for a documented bespoke direction. Specify hierarchy and reading fit; account for language, text expansion, font support and zoom. Do not equate large headings with modernity.
- **Colour and surfaces:** Define surface, text, action, status and feedback roles through the selected system. Make meaning readable without colour alone and validate contrast against applicable interface requirements. Industry conventions can inform context, but do not prescribe palettes: farming software need not be green and banking need not be blue. Retain a coherent, accessible existing brand under the system-selection rules. Include supported themes where required; do not invent a dark-mode requirement.
- **Imagery:** Decide whether imagery establishes identity, explains content, supplies evidence or is unnecessary. Avoid filler illustrations; provide useful text alternatives and media fallbacks. Do not fabricate product evidence or testimonials.
- **Motion:** State a purpose such as showing continuity, change or feedback. Avoid mandatory entrance animations, scroll hijacking and essential hover-only content. Apply project HIG/platform requirements for reduced motion and performance; do not invent budgets.
- **Responsive behaviour:** Adapt hierarchy and controls to available space, input and task. Preserve essential capabilities, current state and context. Consider text scaling, keyboard, touch, pointer and relevant platform conventions. Specify multi-pane collapse or alternate layouts when applicable rather than shrinking the desktop view.

Retain an established coherent visual system or explicit brand/platform brief, and follow the system-selection table in `SKILL.md` otherwise. A bespoke editorial or brand direction is valid when its tokens, components and behaviour are documented and reusable. Utility CSS and component libraries do not supply the missing design decisions automatically. Do not mix competing visual identities merely to show framework coverage.

## Communication and landing-page decisions

Use this method-authored heuristic when a brief involves marketing communication, a landing page or a content-led introduction. Scale it to the requested change; it is not a mandatory section template or conversion checklist.

Identify whether visitors need to understand, read, browse, evaluate, sign up, purchase or contact someone. Mixed purposes can branch. Rank their actual questions: who is this for, what does it offer, how does it work, what distinguishes it, what supports the claims, what does it cost, and what happens next? Use `references/audience-and-page-patterns.md` only when domain prompts would help.

Treat the first viewport as a priority region, not a fixed canvas. Make essential audience, offer and distinguishing information readily discoverable, with a next action where the purpose calls for one. A reading page need not have a transactional CTA. On mobile, a large demonstration can follow the first viewport if essential context and relevant actions remain easy to reach. Avoid fixed fold heights, text/image ratios, section counts and headline word quotas.

Build depth around successive questions: immediate orientation, evaluation, decision, then supporting reference. These are information priorities, not four required sections. Keep price, prerequisites, risks, limitations and recovery at the point where they affect a decision; progressive disclosure must not conceal them.

Choose a representation for the question it answers:

| Representation | Useful when | Evidence and limits |
|---|---|---|
| Actual product screenshot | Showing a software workflow or interface capability | Use a true, relevant screen; label concepts as proposals, and avoid illegible decorative screens |
| Photography | Showing product detail, people, place or contextual identity | Verify relevance and usage rights; stock imagery cannot establish product capability |
| Diagram | Explaining relationships, sequence or a connected workflow | Match actual relationships and distinguish proposed from supported behaviour |
| Table | Comparing plans, specifications or alternatives | Use comparable attributes and expose material costs, exclusions and unknowns |
| Chart | Explaining measured trends or differences | Require source data, units, periods and appropriate uncertainty; never invent metrics |
| Video | Demonstrating change over time or a process that still images cannot explain well | Provide applicable captions, alternatives and loading fallbacks; do not make essential facts video-only |
| Text | Explaining nuance, conditions or a story directly | Use prose when media adds no useful information |

Use the existing object-map gate when audience branches, plans, products or roles change navigation or structure. A copy-only hero adjustment with unchanged structure skips the map with the existing one-line reason. Apply AI-specific guidance only if the actual feature involves AI. Define relevant outcomes using `references/acceptance-and-validation.md`; aesthetics alone cannot establish conversion or retention.

## Extend for specialized requirements

The core procedure applies broadly; its named sources do not cover every modern medium. When requirements exceed their coverage:

1. Identify the actual specialist requirement, target platform/input and consequence of error. Examples include spatial comfort, a chart's uncertainty encoding, professional canvas manipulation, or multi-user edit conflicts.
2. Retain the relevant project/industry conventions and consult applicable official platform or specialist guidance. Check the specific pattern rather than only its landing page. Add a source only when it resolves a real gap.
3. Record source/version/date, reviewed scope and the resulting decision or adaptation. If guidance or evidence cannot be obtained, identify the limitation and provide the best reviewable proposal; do not claim compliance or invent thresholds.
4. Preserve the conditional object-map gate and decision record. Produce or reuse a verified map only when relationships affect the navigation, routes, or screen structure being designed or changed, and use the smallest sufficient map. Existing product complexity alone does not require a map for an unrelated copy or styling fix.
5. Add purpose-specific acceptance checks and proportionate validation with the actual input/device. A flat mockup cannot verify spatial comfort, assistive-technology behavior, real-time conflict handling or measured user outcomes.

For complex charts/maps, consult data-visualization guidance and validate units, scales, uncertainty, comparisons and accessible alternatives. For native, TV, wearable, voice, AR/VR or spatial experiences, use the target platform's interaction/accessibility guidance; web checks alone are insufficient. For commerce, collaboration and creative tools, resolve domain behavior from the brief and established patterns, not invented capabilities. Record uncovered areas rather than calling the method universally validated.

## Define modernity through fitness

Accept visual trends only when they serve the experience and satisfy applicable quality requirements. Do not mandate gradients, glass effects, oversized type, bento grids, animation or card layouts. Support expressive and restrained designs equally when justified. Review the resulting interface for content sufficiency, coherence, platform fit and purpose-specific outcomes; framework citations alone do not establish design quality.
