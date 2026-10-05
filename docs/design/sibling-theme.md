# Design record: sibling theme

Skill: design-decision-method 2.2.4 · Date: 2026-10-05 · Visual system: Web HIG docs site colour theme, hand-authored CSS (no component library) · Project guidelines: Web HIG Quick Reference v1.12.5, archetype content, surface document

Map: skipped — purely visual restyle. Sections, order, and routes are unchanged. One link was added in the existing docs list so this record can be opened from the page.

## 1. Context

- Audience and roles: the same readers as [project-page.md](project-page.md). One person evaluating the method. No new role.
- Experience purpose and primary outcomes: unchanged. Reading and evaluation. The page should also be recognisable as a sibling of the Web HIG site, without being mistaken for it.
- Primary tasks: unchanged. Understand, compare, install, open the repository.
- Cost of error: a visitor treats this page as the Web HIG site, or a colour pair falls below WCAG 2.2 AA. There is still no account, payment, or irreversible action.
- Device, input, language, connectivity: unchanged. Mobile-first web, keyboard, pointer, and touch. English, left to right. Static page. No JavaScript.
- Known facts: the sibling visual source is the published Web HIG docs, `frozonfreak/webhig` commit `0eba4f0`, file `docs/css/site.css`. That file defines the primitive palette and the light semantic tokens. It has no `prefers-color-scheme` block. `HIG.md` §3.1 documents a separate token example, including dark hex values that are not all in `site.css`. The reading layout from [project-page.md](project-page.md) stays: 68ch measure, contents after the hero, sticky contents from 64rem, install paths in `pre`/`code`, one filled action. `docs/` is outside the skill package, so release 2.2.4 is unchanged.
- Assumptions (mark each):
  - Visitors who know the Web HIG site will recognise the shared slate and blue palette, the dark contents chrome, the white cards, and the dark code blocks. (assumption)
  - A wordmark plus a three-bar tile is enough to tell the two sites apart, because the Web HIG site's brand is the words "The Web HIG" with no icon. (assumption)
  - Keeping `font-src 'none'` matters more than downloading Inter. The declared family list matches the sibling. (assumption)

## 2. Object map

Map: skipped — the restyle does not change navigation, routes, or screen structure. The objects in [project-page.md](project-page.md) still describe the page.

## 3. Decisions

| Decision | Frequency | Familiarity | Error cost | Device | Pattern chosen | Reason |
|---|---|---|---|---|---|---|
| Use the Web HIG docs palette instead of the previous green Material roles | Every visit | Readers may know one site and not the other | High if the page invents a third palette, or copies the Web HIG name | Any | Primitive hex values copied from `docs/css/site.css` into `docs/tokens.css`. Page CSS uses the semantic roles | The two sites should read as one family. The hex values are taken from the sibling stylesheet, not invented. |
| Keep a distinct mark and wordmark | Every visit | The Web HIG brand is a text wordmark, "The Web HIG" | High if this page uses that name or the two-tone "open standard" badge | Any | Wordmark "Design Decision Method". Mark is a blue rounded tile with three white bars of different lengths | The bars were already this project's sequence mark. The tile uses `--pr-blue-600` and `--pr-white` from the shared palette. It is not the Web HIG badge. |
| Keep light and dark, even though the sibling stylesheet is light only | Every visit | This page already followed the system scheme | Medium if dark pairs are invented or fail contrast | Any | Dark roles reassign the same primitives. Links and focus use `--pr-blue-400`. Filled buttons stay `--pr-blue-600` with white text | `site.css` has no dark block. Reusing its primitives keeps the family. `HIG.md`'s dark brand `#3b82f6` is not in `site.css` and is 3.98:1 on `#1e293b`, so it is not used. |
| Leave the reading layout in place | Every visit | The previous pass set the measure, the contents placement, and the install blocks | High if a visual match deletes those gains | Any | Same HTML sections and the same breakpoints: contents row after the hero, sticky sidebar from 64rem, 68ch column | The sibling's full-height nav needs a menu button and JavaScript on small screens. This page stays usable without script. |

Adaptation lines (only where departing from a cited source rule):

- Web HIG docs `--muted: var(--pr-slate-500)` / this page uses `--pr-slate-600` for muted text / `#64748b` on the page background `#f4f6f9` is 4.40:1, under the 4.5:1 text minimum. `#475569` on `#f4f6f9` is 7.00:1. Both values are primitives in `site.css`.
- Web HIG docs card border `--border: var(--pr-slate-200)` / cards, sections, and the footer rule use `--pr-slate-500` / `#e2e8f0` on white is 1.23:1. A boundary that shows where a card starts needs 3:1. `#64748b` on white is 4.76:1 and on `#f4f6f9` is 4.40:1.
- Web HIG docs inline code `--code-inline-fg: var(--pr-rose-700)` in every scheme / light mode keeps rose on `#f1f5f9` (5.74:1). Dark mode uses `--pr-blue-400` on `#0f172a` (7.02:1) / `#be123c` on `#0f172a` is 2.84:1.
- Web HIG docs link colour `--accent: var(--pr-blue-600)` on the dark sidebar / text links in dark mode use `--pr-blue-400` / `#1d4ed8` on `#0f172a` is 2.66:1. `#60a5fa` on `#0f172a` is 7.02:1 and on `#1e293b` is 5.75:1. Filled buttons keep white on `#1d4ed8` (6.70:1) in both schemes.
- Web HIG docs load Inter from Google Fonts / this page declares the same family list and does not request the font / the page CSP sets `font-src 'none'`. The list still prefers Inter when it is installed, then the sibling's own fallbacks.
- Web HIG docs eyebrow is 0.8125rem, uppercase, and short ("The Web HIG") / this eyebrow stays a 1rem sentence / the audience line is long. Uppercase tracking would wrap it on a 320px screen and push the actions out of the first view.
- Web HIG docs `h1` is clamped and limited to 22ch / this title uses the existing clamp and no 22ch cap / "Design Decision Method" would wrap early and grow the hero. The first view at 320×568 has to keep the title, the lead, and both actions.
- Web HIG docs body text is the user-agent size, about 1rem, and lead text is 1.125rem / this page keeps body 1.125rem and lead 1.25rem / those sizes are the readability pass. The colour of the lead and of section prose is the sibling's secondary text.
- Web HIG docs code is 0.8125rem / install paths stay 1rem / a path is what the reader copies. The block still uses the sibling's slate-800 background and slate-200 text.
- Web HIG docs cards translate on hover / this page does not move them / the previous record uses no motion. Hover changes colour immediately. `scroll-behavior` stays `auto`.
- Web HIG docs sidebar label is 0.6875rem / "Contents" stays 1rem, with the sibling's uppercase tracking / the label is how a reader finds the list. The tracking and the dark chrome are the family signal.
- Web HIG docs focus ring is 3px `--accent` / same width and offset. Dark mode draws it in `--pr-blue-400` / `#1d4ed8` does not clear 3:1 on the dark page. The offset keeps the ring on the page, including around the blue button.
- `HIG.md` §3.1 dark surface `#090d16` and brand `#3b82f6` / not used / they are not tokens in the sibling stylesheet this page is mirroring, and `#3b82f6` on the site's dark surface `#1e293b` is 3.98:1.

Presentation direction:

- Experience purpose: unchanged. Reading and evaluation.
- Understood first: unchanged. Audience, title, lead, then Get started. View on GitHub stays a text link.
- Composition and density: unchanged column and section order. Surfaces now follow the sibling: gray page, white cards with a 12px radius and the small shadow from `site.css`, a blue filled button with an 8px radius, and install paths in a dark code block.
- Imagery: the three-bar tile in the header and the favicon. Width and height are set on the header SVG. No Web HIG badge, no second logo, no metrics.
- Motion: none.
- Responsive behaviour: unchanged from [project-page.md](project-page.md). The release chip in the header is hidden below 40rem so the wordmark stays on one line at 320px. The release line in the hero remains.

Visual roles and tokens:

- Tokens live in `docs/tokens.css`. Names follow `docs/css/site.css`: `--bg`, `--surface`, `--text`, `--text-secondary`, `--muted`, `--accent`, `--sidebar-bg`, `--code-block-bg`, and the rest listed there. `--link` is added so dark text links can differ from the filled button.
- Light semantic colours match the sibling except the two substitutions above (muted text, component border).
- Dark page background is `--pr-slate-900` (`#0f172a`), the sibling's sidebar. Raised surface and cards are `--pr-slate-800` (`#1e293b`), the sibling's code-block background. Primary text is `--pr-slate-50`. Secondary text is `--pr-slate-300`, which is also `HIG.md`'s dark `--text-secondary`.
- The header and the contents list use the sidebar roles in both schemes, so the chrome matches the sibling's dark nav. Contents links are `--pr-slate-400` on `#0f172a` in light (6.96:1) and `--pr-slate-300` on `#0f172a` in dark (12.02:1).
- Focus: 3px solid `--focus-ring`, offset 2px, matching the sibling. `:focus:not(:focus-visible)` removes it for pointer focus. The skip link is first, with the sibling's accent fill and white text.
- Targets: unchanged. Inline links in a sentence use the line height. Standalone links use at least 2.75rem. There is no form, so error, disabled, and read-only do not apply.
- Forced colours and increased contrast: the existing overrides stay. Increased contrast sets secondary and muted text to the primary text colour and strengthens borders.

### Contrast of the pairs this restyle uses

Ratios are relative luminance, WCAG 2.2. Text needs 4.5:1. A boundary or focus ring needs 3:1.

| Pair | Schemes | Ratio | Role |
|---|---|---|---|
| `#0f172a` on `#f4f6f9` | Light | 16.49:1 | Primary text on the page |
| `#0f172a` on `#ffffff` | Light | 17.85:1 | Primary text on a card |
| `#334155` on `#f4f6f9` | Light | 9.56:1 | Secondary text on the page |
| `#334155` on `#ffffff` | Light | 10.35:1 | Secondary text on a card |
| `#334155` on `#eff6ff` | Light | 9.51:1 | Secondary text on the fit note |
| `#475569` on `#f4f6f9` | Light | 7.00:1 | Muted text on the page |
| `#475569` on `#ffffff` | Light | 7.58:1 | Muted text on a card |
| `#1d4ed8` on `#f4f6f9` | Light | 6.19:1 | Link and focus ring on the page |
| `#1d4ed8` on `#ffffff` | Light | 6.70:1 | Link on a card |
| `#1d4ed8` on `#eff6ff` | Light | 6.16:1 | Link on the fit note |
| `#ffffff` on `#1d4ed8` | Both | 6.70:1 | Label on the filled button and the skip link |
| `#ffffff` on `#1e40af` | Both | 8.72:1 | Label on the hovered button |
| `#be123c` on `#f1f5f9` | Light | 5.74:1 | Inline code |
| `#e2e8f0` on `#1e293b` | Light | 11.87:1 | Code block text |
| `#94a3b8` on `#0f172a` | Light chrome | 6.96:1 | Contents link on the dark bar |
| `#60a5fa` on `#0f172a` | Light chrome, dark links | 7.02:1 | Contents label, dark link, dark focus ring |
| `#64748b` on `#ffffff` | Light | 4.76:1 | Card border |
| `#64748b` on `#f4f6f9` | Light | 4.40:1 | Section rule on the page |
| `#f8fafc` on `#0f172a` | Dark | 17.06:1 | Primary text on the page |
| `#f8fafc` on `#1e293b` | Dark | 13.98:1 | Primary text on a card |
| `#cbd5e1` on `#0f172a` | Dark | 12.02:1 | Secondary text and contents links |
| `#cbd5e1` on `#1e293b` | Dark | 9.85:1 | Secondary text on a card |
| `#94a3b8` on `#1e293b` | Dark | 5.71:1 | Muted text on a card, card border |
| `#60a5fa` on `#1e293b` | Dark | 5.75:1 | Link on a card |
| `#dbeafe` on `#0f172a` | Dark | 14.63:1 | Link hover |
| `#e2e8f0` on `#0f172a` | Dark | 14.48:1 | Code block text |
| `#60a5fa` on `#0f172a` | Dark | 7.02:1 | Inline code |

The fit note in dark mode sits on a 15% `#60a5fa` wash. On the page that wash is about `#1b2c49`. `#cbd5e1` on it is about 9.4:1. `#60a5fa` as the left rule is about 5.5:1 against that wash.

### Web HIG Quick Reference v1.12.5

Archetype: content. Surface: document. The rules already applied in [project-page.md](project-page.md) still apply. This restyle changes these points:

- 58, 59, 60, 61, 62 — semantic tokens now come from the sibling stylesheet. Contrast was recalculated for the new pairs. Status is still in words.
- 64 — dark mode was rechecked because every semantic pair changed. The sibling site itself does not ship a dark theme.
- 81 — still no JavaScript. The sibling's menu button is not copied.
- 82 — the font stack string matches the sibling. The font file is not downloaded.
- 91, 92 — CSP is unchanged, including `font-src 'none'` and `script-src 'none'`.

## 4. Acceptance criteria

| Task, audience, device | Expected outcome | Check or metric | Target (proposed or evidence-based) | Method | Result (or "not tested") |
|---|---|---|---|---|---|
| Developer, phone, first visit | Eyebrow, title, lead, Get started, and View on GitHub are inside a 320×568 view, and Get started is the only filled action | Positions in the hero | Proposed | Headless Chrome, light and dark | Not tested yet |
| Developer on a wide screen | Prose stays within 60–75ch, and the contents list is a sticky sidebar from 64rem | Content box near 68ch | Proposed | Headless Chrome | Not tested yet |
| Reader at 320, 390, and 1280, light and dark | No page-level horizontal scroll. Text and the focus ring meet the ratios above | `scrollWidth` equals `clientWidth`. axe violation count is 0 | Evidence-based (WCAG 2.2 AA, automated subset) | axe-core in headless Chrome | Not tested yet |
| Reader comparing the two sites | This page uses the sibling's slate and blue, dark chrome, cards, and code blocks, and a different name and mark | Side-by-side screenshots | Proposed | Screenshots of both sites | Not tested yet |

## 5. Validation status

- Evidence levels reached: contrast ratios for the token pairs above were calculated on 2026-10-05. Browser, axe, and screenshot checks are not done yet in this draft of the record.
- Accessibility target, what was tested, what was not: target remains WCAG 2.2 AA. A screen reader pass is not planned for this restyle. The calculated pairs are not a full rendered audit.
- Open questions and deferred items:
  - `docs/` stays out of the skill package. Release 2.2.4 is unchanged.
  - Inter is not self-hosted. Machines without Inter use the sibling's fallbacks.
  - The Web HIG site has no dark theme to compare. Dark screenshots are of this page only.
