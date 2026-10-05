# Design record: project page

Skill: design-decision-method 2.2.4 · Date: 2026-10-05 · Visual system: Material 3 roles, hand-authored CSS (no Material library installed) · Project guidelines: none supplied

## 1. Context

- Audience and roles: independent developers and small teams who build interfaces with AI coding agents and do not have a dedicated designer. One reader at a time. No separate admin or reviewer role on this page.
- Experience purpose and primary outcomes: reading and evaluation. A visitor learns what the method is, sees whether it fits, and can start an install or open the repository.
- Primary tasks (frequency, urgency): understand the method (first visit), follow the six steps (first visit), recognize a fit from the examples (first visit), copy the install path for one host (first visit, then occasional re-check), open the repository, the procedure, or the license (occasional). None of these are urgent operational tasks.
- Cost of error: mistaking the method for a UI library or a second quality standard; following an install path the project has not verified; treating an illustration as a measured result. There is no payment, account, or irreversible product action on this page.
- Device, input, language, connectivity: mobile-first web, also wide screens. Keyboard, pointer, and touch. English. Online static page. No offline mode.
- Known facts: the definition, the problem it addresses, the unmeasured time savings, the WebHIG boundary, the six-step workflow, and the install paths are taken from `README.md` and `SKILL.md` for release 2.2.4. License is MIT, copyright 2026 Sastha K L. `docs/` is outside the skill package in `release-manifest.json`, so this page does not bump the skill version. Install paths were recorded in the README as checked on 2026-10-05. Codex personal directory, other hosts, and Claude.ai were already marked not verified.
- Assumptions (mark each):
  - Visitors can read English. (assumption)
  - "Get started" means the install section on this page, and "View on GitHub" means the repository root. (assumption)
  - One long page is enough for this evaluation. A multi-page docs site was not requested. (assumption)
  - A system font stack is acceptable because the project has no brand typeface. (assumption)
  - Host documentation was not re-opened for this revision. The dates and verdicts are carried from the README. (assumption, stated on the page)

## 2. Object map

Map: produced — Method, Step, Example, Install path, and Link are separate objects, and the links between them set the section order and the in-page routes. Top-level navigation on this page is new.

| Object | Relationships | Decision-relevant attributes | Actions |
|---|---|---|---|
| Method | Has an ordered set of Steps. Illustrated by Examples. Obtained through an Install path. Compared with WebHIG, which is a separate project. | Name, release 2.2.4, audience, what it decides, what it does not do, license | Understand, compare, decide to install |
| Step | Belongs to Method. Order is fixed by `SKILL.md`. Step 4 points at this record. | Order, name, what to do, when a step is skipped | Read in order, open the procedure |
| Example | Illustrates Method and one or more Steps. Not a measured case study. | Situation, what the method asks, no metrics | Recognize a fit |
| Install path | Belongs to one host. Points at the Method files. | Host, directories, verification status, check date | Copy the folder, confirm in that host's docs |
| Link | From a section to the repository, the procedure, references, this record, or the license | Label, destination, why it is offered | Follow |

Routes derived from the map:

- `#top` — Method identity, audience, and the two actions (Get started → `#start`, View on GitHub → repository)
- `#about` — what repeated guesswork the Method addresses, including the unmeasured time savings
- `#how` — the six Steps, in workflow order
- `#webhig` — Method compared with WebHIG
- `#examples` — three Examples
- `#start` — Install paths, including hosts marked not verified
- `#docs` — Links to the repository, the procedure, the references, this record, and the license

## 3. Decisions

| Decision | Frequency | Familiarity | Error cost | Device | Pattern chosen | Reason |
|---|---|---|---|---|---|---|
| Open with the definition, the audience, and two actions | First visit | Readers know a project page; they do not know this method | High if the first screen is vague or sounds like a component library | Phone first | One column: eyebrow, title, lead, then the two actions, then the fit line | The evaluation starts from what it is and who it is for. The actions sit above the fit line so they stay in view on a short phone. Reading does not require a single action, so both install and source are offered. |
| Explain the workflow as six numbered steps | First visit | The names match `SKILL.md` | Medium if the gate or the evidence labels are dropped | Any | Ordered list, one heading and one short explanation per step | The sequence is the method. A card grid would hide the order. |
| Show WebHIG as a comparison, not a merged standard | Occasional, when the two projects are confused | Familiar only to people who know both repos | High if this page copies WebHIG rules into a second standard | Any | Three grouped definition lists, plus one link to the WebHIG repository | The rows are the README's boundary. The link is the real project, not a restatement of its requirements. |
| Use illustrations instead of case studies | First visit | Readers may treat stories as proof | High if a number or a quote is invented | Any | Three situations, each with "what the method asks," introduced as illustrations | The audience needs to recognize the correction loop. There are no measured results to show. |
| List install paths with a verification line | First visit, then re-check | Host directories differ and change | High if an unverified path is presented as checked | Any | One block per host, directory in `code`, status in words | The README's table is the source. "Checked" and "Not verified" are text, not color. |
| Keep deeper material as links | Occasional | Readers who want the procedure already expect a repository | Low | Any | A link list: repository, `SKILL.md`, README, references, template, this record, changelog, docs, license | This page is the introduction. It does not replace the procedure. |

Adaptation lines (only where departing from a cited source rule):

- Material 3 as the fallback for other web work with no system, with implementation support checked / this page uses Material 3 role names as hand-authored custom properties and a system font stack, and does not load a Material component library / the page is static, the project has no brand system and no installed Material version, and the cost of a wrong color is contrast, which is calculated directly. Shipping a library would add weight without a component set to inherit.
- A full ORCA object map / a five-row map of the page's objects / the page has few objects and one route. The smallest map that sets the sections is enough. The page says this is not a completed ORCA method.

Presentation direction:

- Experience purpose: reading and evaluation.
- Understood first: what the method is, who it is for, and the two actions.
- Composition and density: one reading column, about 42rem, sections in the order a visitor decides. Full-width bands for the masthead, the opening, and the footer. No metric cards, no logos of other systems, no photographs.
- Imagery: an original three-bar mark for the favicon, the header, and the social image. The bars are a sequence, not a borrowed logo.
- Motion: none. Nothing essential depends on animation.
- Responsive behaviour: the same sections at every width. Buttons grow to the row on narrow screens. The WebHIG pairs stack, then sit in two columns from 40rem. Text uses rem so it enlarges with the root font size. The column is `min(100%, 42rem)` so it does not force a horizontal scroll.

Visual roles and tokens, or exact verified inherited tokens/components. New focus, errors and disabled/read-only behaviour still need checks:

- Tokens live in `docs/tokens.css`. Light and dark follow `prefers-color-scheme`. `prefers-contrast: more` strengthens borders and secondary text. There is no theme toggle and no JavaScript.
- Roles: surface, surface-container, surface-container-high, on-surface, on-surface-variant, primary, on-primary, primary-hover, primary-container, on-primary-container, outline, outline-variant, focus-ring, inverse-surface, inverse-on-surface, link.
- Type: system-ui stack. No web font, so type does not arrive late and shift the layout. Display, headline, title, body, and label sizes are in the token file. The social image is a raster PNG. Inter is drawn into those pixels and is not loaded by the page.
- Shape: 0.5rem radius on buttons and the fit line. Links in prose are underlined. Buttons are identified by fill or border.
- Focus: 3px solid ring, 3px offset, on `:focus-visible`. The skip link appears at the top of the viewport when focused. `main` is the skip target (`tabindex="-1"`).
- Errors, disabled, and read-only: no form controls on this page. Not applicable.
- Forced colors: buttons, the skip link, and the fit line keep a system border and system text.

## 4. Acceptance criteria

| Task, audience, device | Expected outcome | Check or metric | Target (proposed or evidence-based) | Method | Result (or "not tested") |
|---|---|---|---|---|---|
| Developer, phone, first visit | Can say what the method is, who it is for, and find Get started and View on GitHub in the opening view | Those items are in the hero, and both actions are inside the viewport | Proposed | Headless Chrome, light and dark | Pass at 320×568, 375×667, 390×844, and 1280×800. On 320×568 the fit line starts at the bottom edge. The sentence that this is not a UI library is in the next section, so the actions stay in view on that short screen. |
| Developer reading the steps | The six steps match `SKILL.md` order, and the object map is conditional | Step order and the skip condition are stated | Proposed | Heuristic comparison with `SKILL.md` | Author review: order matches, and step 3 states when to skip the map. Not a user test. |
| Developer choosing a host | Can find Cursor, Claude Code, Gemini CLI, and Codex paths, and can see which hosts are not verified | Path text matches the README. "Not verified" is visible text. | Proposed | Heuristic comparison with `README.md` | Author review: paths and the 2026-10-05 check note match the README. Codex personal directory, other hosts, and Claude.ai say not verified. |
| Any reader, text and UI | Text at least 4.5:1, UI boundaries and the focus ring at least 3:1 | Contrast ratio of the token pairs in use | Evidence-based (WCAG 2.2 AA) | Automated calculation, relative luminance, 2026-10-05 | Pass for the pairs checked. Lowest text pair 5.98:1 (link on the code chip, light). Lowest boundary 3.80:1 (divider on the page surface, light). Focus ring against page and hero backgrounds is above 10:1. Not a full-page rendered audit. |
| Keyboard user | The skip link is first, and focus is visible | Focus order and a visible ring | Evidence-based (WCAG 2.2 AA 2.4.1, 2.4.7) | Headless Chrome tab walk | First Tab focused "Skip to main content" with a 3px solid outline, and the link was visible. Further tabs on the desktop view reached the brand, the in-page nav, both hero actions, and later links, each with a 3px outline. Not every link was tabbed, and a screen reader was not used. |
| Reader at 320px CSS width and at 400% zoom | Content reflows without a horizontal scroll, except where a two-dimensional layout truly needs it | No document overflow | Evidence-based (WCAG 2.2 AA 1.4.10) | Headless Chrome | No document overflow at 320, 375, 390, or 1280 CSS pixels. No document overflow at 320px width with the root font set to 32px. |

## 5. Validation status

- Evidence levels reached: proposed targets, an author heuristic review of the copy against `SKILL.md` and `README.md`, an automated contrast calculation, an axe-core run in headless Chrome, and headless checks of reflow, the opening viewport, and a partial keyboard walk. No user research. No Lighthouse score. No screen reader pass. This is not a conformance claim.
- Accessibility target, what was tested, what was not: target is WCAG 2.2 AA. Contrast of the stated token pairs was calculated (lowest text pair 5.98:1, lowest boundary 3.80:1). axe-core, tags `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa`, and `wcag22aa`, reported no violations on the rendered page. That does not cover every criterion. A screen reader was not used. Lighthouse was not run.
- Open questions and deferred items:
  - Host paths were not re-checked against the vendor docs for this revision.
  - On a 320×568 screen the fit line is only partly in the opening view. The actions are fully in view.
  - Time saved by the method remains unmeasured and is stated that way on the page.
  - `docs/` is not in the skill package, so release 2.2.4 is unchanged.
