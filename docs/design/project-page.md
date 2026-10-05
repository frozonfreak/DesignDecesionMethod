# Design record: project page

The colour theme in this record was replaced by a later visual restyle. Read [sibling-theme.md](sibling-theme.md) for the current tokens, mark, and contrast notes. The reading layout in this record still applies: 68ch measure, contents after the hero, sticky contents from 64rem, install paths in `pre`/`code`, and one filled action.

Skill: design-decision-method 2.2.4 · Date: 2026-10-05 · Visual system: Material 3 roles, hand-authored CSS (no Material library installed) · Project guidelines: Web HIG Quick Reference v1.12.5, archetype content, surface document

## 1. Context

- Audience and roles: independent developers and small teams who build interfaces with AI coding agents and do not have a dedicated designer. One reader at a time. No separate admin or reviewer role on this page.
- Experience purpose and primary outcomes: reading and evaluation. A visitor learns what the method is, sees whether it fits, and can start an install or open the repository.
- Primary tasks (frequency, urgency): understand the method (first visit), follow the six steps (first visit), recognize a fit from the examples (first visit), copy the install path for one host (first visit, then occasional re-check), open the repository, the procedure, or the license (occasional). None of these are urgent operational tasks.
- Cost of error: mistaking the method for a UI library or a second quality standard; following an install path the project has not verified; treating an illustration as a measured result. There is no payment, account, or irreversible product action on this page.
- Device, input, language, connectivity: mobile-first web, also wide screens. Keyboard, pointer, and touch. English, left to right. Online static page. No offline mode.
- Known facts: the definition, the problem it addresses, the unmeasured time savings, the WebHIG boundary, the six-step workflow, and the install paths are taken from `README.md` and `SKILL.md` for release 2.2.4. License is MIT, copyright 2026 Sastha K L. `docs/` is outside the skill package in `release-manifest.json`, so this page does not bump the skill version. Install paths were recorded in the README as checked on 2026-10-05. Codex personal directory, other hosts, and Claude.ai were already marked not verified. This revision is a readability and Web HIG pass. It does not add claims, metrics, or host paths.
- Assumptions (mark each):
  - Visitors can read English. (assumption)
  - "Get started" means the install section on this page, and "View on GitHub" means the repository root. (assumption)
  - One long page is enough for this evaluation. A multi-page docs site was not requested. (assumption)
  - A system font stack is acceptable because the project has no brand typeface. (assumption)
  - Host documentation was not re-opened for this revision. The dates and verdicts are carried from the README. (assumption, stated on the page)
  - A reading measure of 68ch is comfortable for this body size. The requested range was 60–75ch. (assumption)

## 2. Object map

Map: reused — Method, Step, Example, Install path, and Link are the same objects as the previous record. The contents list now includes the existing `#about` route, which was already a section and was missing from the earlier nav. No new objects.

| Object | Relationships | Decision-relevant attributes | Actions |
|---|---|---|---|
| Method | Has an ordered set of Steps. Illustrated by Examples. Obtained through an Install path. Compared with WebHIG, which is a separate project. | Name, release 2.2.4, audience, what it decides, what it does not do, license | Understand, compare, decide to install |
| Step | Belongs to Method. Order is fixed by `SKILL.md`. Step 4 points at this record. | Order, name, what to do, when a step is skipped | Read in order, open the procedure |
| Example | Illustrates Method and one or more Steps. Not a measured case study. | Situation, what the method asks, no metrics | Recognize a fit |
| Install path | Belongs to one host. Points at the Method files. | Host, directories, verification status, check date | Copy the folder, confirm in that host's docs |
| Link | From a section to the repository, the procedure, references, this record, or the license | Label, destination, why it is offered | Follow |

Routes derived from the map:

- `#top` — Method identity, audience, one primary action (Get started → `#start`), and a secondary link (View on GitHub → repository)
- `#about` — what repeated guesswork the Method addresses, including the unmeasured time savings
- `#how` — the six Steps, in workflow order
- `#webhig` — Method compared with WebHIG
- `#examples` — three Examples
- `#start` — Install paths, including hosts marked not verified
- `#docs` — Links to the repository, the procedure, the references, this record, and the license

## 3. Decisions

| Decision | Frequency | Familiarity | Error cost | Device | Pattern chosen | Reason |
|---|---|---|---|---|---|---|
| Open with eyebrow, title, lead, then one primary action | First visit | Readers know a project page; they do not know this method | High if the first screen is vague, or if two equal buttons compete | Phone first | One column: eyebrow, h1, lead, filled link "Get started", then a text link "View on GitHub" | The evaluation starts from what it is and who it is for. Reading has one next step. The repository stays available without matching the primary button. |
| Keep body text inside 68ch | Every visit | Long lines are harder to track | Medium if a wide screen stretches the prose | Any | `--measure: 68ch` on the content column, with padding outside that measure | 68ch is inside the 60–75ch range. The column is a max, so narrow screens use the viewport. |
| Show a contents list on every width | First visit, then jumps | Readers expect in-page links on a long document | Low | Narrow: a row after the hero that sticks on scroll and scrolls sideways. From 64rem: a sticky sidebar | A `nav` labelled "Contents", after the hero, with links to every section including `#about` | The earlier nav omitted "What it is for" and sat above the title, which pushed the actions off a 320×568 screen. Placing it after the hero keeps eyebrow, title, lead, and both actions in that first view. It then sticks so later sections stay one tap away. The sidebar appears only when both columns fit. Tab order follows the hero, then the contents list, so the primary action stays first. |
| Explain the workflow as six numbered steps | First visit | The names match `SKILL.md` | Medium if the gate or the evidence labels are dropped | Any | Ordered list, one heading and short paragraphs per step | The sequence is the method. A card grid would hide the order. Paragraph breaks follow the existing sentences. |
| Show WebHIG as a comparison, not a merged standard | Occasional, when the two projects are confused | Familiar only to people who know both repos | High if this page copies WebHIG rules into a second standard | Any | Three grouped definition lists. One column on narrow screens, two columns from 48rem. One link to the WebHIG repository | The groups are the README's boundary. Stacking keeps the phrases readable at 320px. The link is the real project. |
| Use illustrations instead of case studies | First visit | Readers may treat stories as proof | High if a number or a quote is invented | Any | Three cards, each with a "Situation." label and a "What the method asks." label | The labels make the two parts scannable. There are no measured results to show. |
| Put install paths in copyable blocks | First visit, then re-check | Host directories differ and change | High if an unverified path is presented as checked | Any | One card per host. Each directory is a `pre`/`code` block. "or" stays between alternatives. Unverified hosts stay in words | A path is what the reader copies. Inline code in a sentence was hard to select. No path was added that the README does not state. Cursor's home directory stays "the same two paths under your user home." |
| Keep deeper material as links | Occasional | Readers who want the procedure already expect a repository | Low | Any | A link list: repository, `SKILL.md`, README, references, template, this record, changelog, docs, license. Each link is on its own line, with the description under it | This page is the introduction. It does not replace the procedure. |

Adaptation lines (only where departing from a cited source rule):

- Material 3 as the fallback for other web work with no system, with implementation support checked / this page uses Material 3 role names as hand-authored custom properties and a system font stack, and does not load a Material component library / the page is static, the project has no brand system and no installed Material version, and the cost of a wrong color is contrast, which is calculated directly. Shipping a library would add weight without a component set to inherit.
- A full ORCA object map / the five-row map above, reused / the page has few objects and one route. The smallest map that sets the sections is enough. The page says this is not a completed ORCA method.
- Web HIG Quick 65 (container queries for multi-context components) / no container queries / this page is one document column, not a component placed in several parents. Adding a container only to satisfy the rule would violate the preference for the simplest implementation.

Presentation direction:

- Experience purpose: reading and evaluation.
- Understood first: audience, what the method is, then Get started. View on GitHub is the secondary link.
- Composition and density: one reading column, 68ch, sections in the order a visitor decides. More space between paragraphs (`--space-l`) and between sections (`--space-2xl`, `--space-3xl` from 48rem). Cards only where a group is a single object (an example, a host, a comparison row). No metric cards, no logos of other systems, no photographs.
- Imagery: the existing three-bar mark in the header and favicon. The bars are a sequence, not a borrowed logo. Width and height are set on the SVG.
- Motion: none. `scroll-behavior` stays `auto`, including under `prefers-reduced-motion`. Nothing essential depends on animation. No `transition`.
- Responsive behaviour: the same sections at every width. At 320 and 390 the contents row comes after the hero, sticks while the rest of the page scrolls, and scrolls sideways. The primary link is full width, and comparison pairs stack. From 64rem the contents list is a sticky sidebar beside the column. Text uses rem so it enlarges with the root font size. Comparison grids use `minmax(0, 1fr)` so long labels wrap at 200% text instead of widening the page.

Visual roles and tokens, or exact verified inherited tokens/components. New focus, errors and disabled/read-only behaviour still need checks:

- Tokens live in `docs/tokens.css`. Page CSS in `docs/page.css` references those tokens. Light and dark follow `prefers-color-scheme`. `prefers-contrast: more` strengthens borders, secondary text, and the focus width. Print resets to a light high-contrast set in the token file. There is no theme toggle and no JavaScript.
- Type scale: display, headline, title, lead, body (1.125rem), label (1rem), code (1rem). Line heights are tokens. Weights are 400, 600, and 700. The earlier 650 weight was dropped because a system font may not provide it.
- Space scale: 0.125rem through 4.5rem. The content column is `68ch` plus the inline padding, so the prose measure stays 68ch when the viewport is wide.
- Focus: a 0.1875rem outer ring in `--on-surface` and a 0.1875rem inner gap in `--surface-container`, so the ring is visible on the page and on the filled primary link. `:focus:not(:focus-visible)` removes the ring for pointer focus. The keyboard ring stays. The skip link is first and becomes visible when focused.
- Targets: text links in a sentence use the line height. Standalone links (contents, primary action, secondary action, doc titles) use at least 2.75rem block size. The 1.5rem token is the 24px floor.
- Errors, disabled, and read-only: no form controls on this page. Not applicable.
- Forced colors: buttons, the skip link, cards, code blocks, and the contents bar keep a system border and system text. Focus uses `Highlight`.

### Web HIG Quick Reference v1.12.5

Archetype: content. Surface: document. Applied on this page:

- 6, 8, 9, 11, 13, 14, 16, 18, 19, 20 — one primary link styled as a button, secondary action is an underlined link, contents and footer offer a next step, hero is first in `main`, mobile rules come before the wide layout, targets are spaced.
- 21, 22 — section URLs are the hashes above. There are no tabs, filters, or sorts.
- 25, 26, 27, 28 — one `main`, `lang="en"` and `dir="ltr"`, a unique title, and `header`, `nav`, `footer`.
- 29 — crawlable HTML, canonical URL, description, and social meta. JSON-LD was not added, so `script-src` can stay `'none'`.
- 58, 59, 60, 61, 62, 63, 64 — semantic tokens, status in words ("Checked", "Not verified"), contrast rechecked in both schemes, focus ring kept.
- 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 79 — native links, skip link, keyboard, visible focus, 24px floor and 44px on primary and contents links, no motion, zoom not disabled. The header mark is decorative (`aria-hidden`).
- 81, 82, 83, 84, 85, 89, 90 — no JavaScript, system fonts, SVG width and height, no lazy-loaded hero image, no `transition: all`, no new dependency.
- 91, 92 — no secrets. The meta CSP now also sets `script-src 'none'`, `font-src 'none'`, `connect-src 'none'`, `media-src 'none'`, and `object-src 'none'`.

Not applied, because this static document has nothing those rules govern:

- 7 — no network action. Hover and focus change immediately. There is no control that waits on a request.
- 10, 12, 15, 23, 24, 30 — no task state, settings panel, modal, form, command palette, or search.
- 17 — no component library exists in this repo. The page keeps the hand-authored CSS it already had.
- 31–40, 41–49, 50–57, 73, 78, 80 — no async state, destructive action, form, modal, or live update.
- 65 — container queries. See the adaptation line above.
- 86, 87 — no animation, so there is no duration to tokenize.
- 88 — no data table over 100 rows.
- 93–98 — no user-generated content, cookies, sessions, or permission prompts.

## 4. Acceptance criteria

| Task, audience, device | Expected outcome | Check or metric | Target (proposed or evidence-based) | Method | Result (or "not tested") |
|---|---|---|---|---|---|
| Developer, phone, first visit | Eyebrow, title, lead, Get started, and View on GitHub are recognizable, and Get started is the only filled action | Those items are in the hero in that order, and both actions are inside a 320×568 viewport | Proposed | Headless Chrome, light and dark, 320×568, 390×844, and 1280×800 | Pass. On 320×568 the secondary link ends at 556px, inside the 568px viewport. The fit line starts below that edge. On 390×844 the contents row is also inside the first viewport. |
| Developer reading the page | Body column stays within 60–75ch on a wide screen, and text wraps with no page-level horizontal scroll at 320px | Content box about 68ch; `scrollWidth` equals `clientWidth` | Proposed | Headless Chrome | Pass. At 1280 the content box is 67.98ch. At 320 and 390 the column uses the viewport (28ch and 35ch), which is the narrow-screen case, not a wide line. No page-level horizontal overflow at those widths. |
| Developer choosing a host | Can find Cursor, Claude Code, Gemini CLI, and Codex paths, and can see which hosts are not verified | Path text matches the README. "Not verified" is visible text. Paths are in `pre`/`code` | Proposed | Heuristic comparison with `README.md` | Author review: paths and the 2026-10-05 check note match the README. Codex personal directory, other hosts, and Claude.ai say not verified. Cursor's home paths are not spelled out. |
| Developer reading the steps | The six steps match `SKILL.md` order, and the object map is conditional | Step order and the skip condition are stated | Proposed | Heuristic comparison with `SKILL.md` | Author review: order matches, and step 3 states when to skip the map. Not a user test. |
| Any reader, text and UI | Text at least 4.5:1, UI boundaries and the focus ring at least 3:1, in light and dark | Contrast ratio of the token pairs in use | Evidence-based (WCAG 2.2 AA) | Relative luminance, 2026-10-05 | Pass for the pairs checked. Lowest text pair 5.98:1 (link on the code background, light). Lowest boundary 3.80:1 (divider on the page surface, light). Focus gap on the primary link is 9.15:1 light and 8.72:1 dark. Not a full-page rendered audit. |
| Keyboard user | The skip link is first, focus is visible, and in-page links move to the section without the sticky contents bar covering the heading | Focus order, a visible ring, and `scroll-padding-top` | Evidence-based (WCAG 2.2 AA 2.4.1, 2.4.7, 2.4.11) | Headless Chrome | Pass for the checks run. First Tab focused "Skip to main content" (about 219×46 CSS px, 3px solid outline). Enter moved focus to `main`. The next Tab focused "Get started". After a jump to `#start`, the heading top was 121px and the stuck contents bar ended at 61px, so they did not overlap. Not every link was tabbed. A screen reader was not used. |
| Reader at 320px CSS width and at 200% text | Content reflows without a page-level horizontal scroll | No document overflow | Evidence-based (WCAG 2.2 AA 1.4.4, 1.4.10) | Headless Chrome, root font 32px at 320px width | Pass. `scrollWidth` equalled `clientWidth` (320). Contents links scroll inside their row. That row does not widen the page. |
| Automated accessibility | No axe violations for WCAG 2.x A/AA tags that the runner supports | axe-core violation count | Evidence-based (WCAG 2.2 AA, automated subset) | axe-core 4.13.0 in headless Chrome. Tags `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa`, `wcag22aa` | Pass. Zero violations at 320 light, 390 dark, and 1280 light and dark. `wcag22a` is not a tag in this axe build; 2.2 AA rules ship as `wcag22aa`, including target size. This is not every WCAG criterion. |

## 5. Validation status

- Evidence levels reached: proposed targets, an author heuristic review of the copy against `SKILL.md` and `README.md`, an automated contrast calculation of the token pairs, an axe-core 4.13.0 run, and headless Chrome checks of the first viewport, reflow, 200% text, a jump under the sticky contents bar, and a partial keyboard walk. No user research. No Lighthouse score. No screen reader pass. This is not a conformance claim.
- Accessibility target, what was tested, what was not: target is WCAG 2.2 AA. Contrast of the stated token pairs was calculated (lowest text pair 5.98:1, lowest boundary 3.80:1). axe-core reported no violations for the tags above. A screen reader was not used. Lighthouse was not run. On a wide screen the contents list is visually to the left while it follows the hero in tab order, so the primary action stays first.
- Open questions and deferred items:
  - Host paths were not re-checked against the vendor docs for this revision.
  - Time saved by the method remains unmeasured and is stated that way on the page.
  - `docs/` is not in the skill package, so release 2.2.4 is unchanged.
  - JSON-LD was omitted so the page can keep `script-src 'none'`.
