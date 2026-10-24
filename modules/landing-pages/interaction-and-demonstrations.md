# Interaction and demonstrations

Read [module scope and section routing](GUIDE.md) first. Numbered sections below retain ULPG v0.4.0 wording.

## Retained DDM representation refinements

These DDM heuristics supplement section 6 without changing ULPG's requirement levels. Match diagrams to actual relationships and distinguish proposed from supported behavior. For charts, retain source data, units, periods and appropriate uncertainty. For comparisons, use comparable attributes and expose material exclusions and unknowns. Verify photography usage rights; stock imagery cannot establish product capability. Keep screenshots legible enough to explain the relevant workflow. Choose video when change over time needs explanation, with applicable captions, alternatives and loading fallbacks. Use prose when media adds no useful information.

On mobile, a large demonstration can follow the first viewport if essential context and relevant actions remain easy to reach. This is a contextual choice, not a fold height or text/image ratio rule.

## 6. Visual representation

Select representations by their communicative purpose:

| Purpose | Suitable representation |
|---|---|
| Establish context or emotion | Authentic photography |
| Demonstrate software | Real product screenshots |
| Explain a sequence | Diagram or interactive walkthrough |
| Compare alternatives | Table or structured comparison |
| Show a trend | Chart with readable data |
| Show physical products | Accurate product photography |
| Demonstrate interaction | Accessible video or interactive example |
| Explain a concept | Illustration if it adds understanding |
| Present exact facts | Text, lists or tables |

- **MUST:** Make essential meaning available as accessible text or equivalent content.
- **MUST NOT:** Fabricate product screenshots, testimonials, results or customer evidence.
- **SHOULD:** Prefer meaningful imagery over decorative stock images.
- **SHOULD:** Optimize image loading and reserve layout space.
- **MAY:** Include interactive demonstrations when they materially aid understanding.

A text-heavy page is not inherently inferior to a visual-heavy one.

### 6.1 Interactive demonstrations

- **SHOULD:** Choose an interactive demonstration only when participation explains a capability better than a screenshot, diagram, video or text; consider effort, accessibility and loading cost.
- **MUST:** Represent capabilities and limitations accurately and identify illustrative/sample data, simulated behavior and live functionality where visitors could confuse them. Illustrative mockups must be clearly labeled and must not be presented as real product screenshots or evidence that unavailable functionality exists.
- **MUST NOT:** Imply that a simulated action sent a message, changed an account, completed a purchase or executed another real action.
- **SHOULD:** Provide a meaningful static explanation or equivalent fallback that preserves essential understanding when the demonstration is unavailable. Label a fallback so it is not mistaken for an operable control.

See section 11 for interaction and enhancement behavior.

## 10. Responsive, accessible and localized experiences

### 10.1 Accessibility and responsiveness

Landing pages **MUST** meet applicable project accessibility obligations and **SHOULD** target [WCAG 2.2 AA](https://www.w3.org/TR/WCAG22/) as the baseline where no stricter requirement applies. Teams adopting Web HIG must follow its applicable normative requirements.

Core expectations include semantic headings, logical reading order, keyboard accessibility, visible focus, sufficient contrast, useful image alternatives, usable targets, responsive reflow, resizing, accessible media and reduced-motion support.

- **MUST:** Preserve essential meaning, content and actions across supported viewports.
- **MUST:** Not depend exclusively on hover or motion for essential actions.
- **SHOULD:** Test representative mobile, tablet and desktop contexts.

### 10.2 Layout elasticity and localized content

Text expansion differs by language, phrase, script, context and interface element. A single horizontal expansion percentage cannot guarantee localization quality.

- **MUST:** Preserve critical text, meaning and functionality without unintended clipping, overlap or inaccessible controls in the locales the product supports.
- **SHOULD:** Prefer content-driven sizing, flexible wrapping and resilient layout over brittle fixed-height text containers; a fixed size is permissible only if content remains accessible and its constraints are justified.
- **SHOULD:** Test translated navigation, CTA labels, cards, prices and form content across representative viewport and zoom settings.
- **SHOULD:** Verify directionality, logical properties and bidirectional behavior when right-to-left or mixed-direction languages are supported.
- **SHOULD:** Test font support, line height and character shaping for non-Latin scripts, including relevant languages such as Tamil.
- **MAY:** Use 40% text expansion as **one stress-test heuristic**, not a universal MUST threshold or proof of multilingual readiness. Define any project-specific expansion tests and failure criteria explicitly.

## 11. Motion and interaction

Motion may communicate feedback, continuity, spatial relationships or narrative.

- **MUST:** Preserve essential content and actions without animation.
- **MUST:** Respect applicable reduced-motion requirements.
- **SHOULD:** Prefer motion with an identifiable purpose.
- **MUST NOT:** Make scroll-controlled animation the only route to essential information.
- **SHOULD:** Avoid unnecessary animation on routine controls.
- **MAY:** Use expressive sequences or interactive storytelling when suitable.

### 11.1 Progressive enhancement and demonstration states

- **SHOULD:** Build from meaningful content and supported essential routes, then add optional demonstrations or storytelling. If an essential task needs scripting or a service, explain dependencies and provide a useful recovery route when unavailable.
- **MUST:** Keep demonstrations operable with applicable keyboard and assistive-technology support; do not rely solely on dragging, hover or motion for essential meaning or actions.
- **SHOULD:** Address loading, unavailable, error, completion and reset states as relevant, including slow or failed enhancement. Preserve the static explanation or equivalent fallback described in section 6.1.
- **MUST:** Distinguish simulated completion from real execution in feedback as well as initial labels.
