# Entry and navigation

Read [module scope and section routing](GUIDE.md) first. Numbered sections below retain ULPG v0.4.0 wording.

## 3. Establish context before design

Before selecting layouts, typography, imagery or color, identify:

| Dimension | Required consideration |
|---|---|
| Audience | Who will visit the page? |
| Purpose | Why does the page exist? |
| Visitor intent | What brought visitors here? |
| Familiarity | What do visitors already understand? |
| Visit context | What do first-time and returning visitors need to discover, find again or resume? |
| Primary questions | What must they know to proceed? |
| Decision | What choice or action is expected? |
| Trust requirements | What claims require evidence? |
| Device | How and where is the page used? |
| Language | Which languages and reading conventions matter? |
| Connectivity | Are low-bandwidth or unreliable networks important? |
| Brand | Which existing visual conventions must be preserved? |
| Success | What observable outcome demonstrates effectiveness? |

- **MUST:** Identify the page's primary audience and purpose.
- **MUST:** Preserve applicable existing brand, accessibility and platform requirements unless a redesign is explicitly intended and approved; legal and accessibility obligations remain applicable.
- **SHOULD:** Identify secondary audiences and determine whether they need separate journeys.
- **SHOULD:** Identify differences between first-time and returning visitor needs using available evidence; record assumptions without assuming an account or tracking is needed.
- **MAY:** Develop personas or journey maps when multiple audiences or complex decisions justify them.

Do not assume that demographic categories alone determine visual preferences or usability needs.

## 4. Information hierarchy

### 4.1 Primary hierarchy

Organize information according to visitors' decision needs. A typical commercial page may progress through: **relevance → value → explanation → suitability → evidence → commitment**. An editorial page may instead emphasize subject, context, reading and exploration. These are information needs, not mandatory page sections.

- **MUST:** Make the primary purpose identifiable without exploration of unrelated content.
- **MUST:** Keep information necessary for a decision discoverable before that decision.
- **SHOULD:** Prioritize information by relevance and consequences rather than internal business organization.
- **SHOULD:** Use progressive disclosure for optional complexity.
- **MUST NOT:** Remove essential information solely to create whitespace or a shorter page.

### 4.2 Above the fold

The first viewport is the initially visible portion of a page; its dimensions vary by device, browser UI, zoom and settings. It **SHOULD** communicate the subject or offering, relevant audience where needed, primary value or message, and a route to the next meaningful action or content.

A commercial landing page commonly has a headline, supporting text, primary action and meaningful visual. A recognizable product, service-selection interface or editorial subject can instead communicate the primary message without conventional benefit-led copy. Add context where recognition cannot reasonably be assumed. No universal hero height, word count or image percentage applies.

- **MUST:** Make the essential subject, offering or task understandable without requiring animation, a carousel or a hidden panel.
- **SHOULD:** Make the primary next step discoverable early.
- **MUST NOT:** Compress information until readability or comprehension suffers.
- **MAY:** Let imagery continue below the initial viewport, especially on narrow screens.

### 4.3 Below the fold

Depending on the page, useful depth may include problems and benefits, capabilities, workflows, examples, pricing and terms, comparisons, evidence, FAQs, related content and contact or exploration routes.

- **SHOULD:** Arrange content in a meaningful progression, avoiding repetitive promotion.
- **MUST:** Keep essential information accessible without a required animation or scroll sequence.
- **MAY:** Provide summaries, anchor navigation, expandable details or dedicated pages.

### 4.4 Page length

No universal page-length limit applies. Choose length according to complexity, visitor familiarity, decision consequences and necessary evidence.

- **SHOULD:** Remove repetitive sections that add no understanding.
- **MUST NOT:** Require a fixed number of sections across unrelated websites.

### 4.5 Page entry and hero patterns

Select the initial experience by visitor intent, familiarity and page purpose. A hero is one possible presentation, not a required component.

| Illustrative pattern | When it may fit | Initial viewport emphasis | Useful deeper content |
|---|---|---|---|
| Proposition-first | Visitors need to understand an unfamiliar offering | Clear proposition, context and next step | Capabilities, suitability and evidence |
| Product-first | The product is the main subject and recognition is supported | Accurate product representation with necessary identification | Specifications, options, limitations and availability |
| Task-first | Visitors arrive to complete a known task | Search, service selection or task entry | Results, navigation help and contextual information |
| Discovery-first | Visitors need to explore an assortment or range | Categories, collections or useful exploration routes | Comparisons, filtering and offering details |
| Editorial-first | Reading, a story or a brand subject is the purpose | Recognizable subject and route into the narrative | Context, sources and related content |

- **MUST:** Justify the selected entry pattern using intent, familiarity and purpose; record the rationale in the brief or decision record.
- **SHOULD:** Check that the pattern makes the subject and next step understandable to relevant visitors, including those arriving through deep links.
- **MAY:** Combine patterns or vary them across routes, audiences and devices when justified, while preserving essential information and supported journeys.

These categories are illustrative, not exhaustive templates or industry assignments. Brand recognition alone does not establish comprehension for every audience.

### 4.6 Discovery and navigation architecture

Choose how visitors find the offering or content they need, beyond the initial viewport.

- **SHOULD:** Evaluate search, categories, audience routes, product families, contextual navigation and deep links against the content range and visitor tasks. A simple page may need only a few direct links.
- **SHOULD:** Use labels visitors understand and preserve orientation between entry points, related content and detail pages; internal organization need not dictate navigation.
- **MUST:** Keep decision-critical information and supported destinations reachable across relevant devices and input methods.
- **SHOULD:** When search or filtering is offered, provide understandable results, empty/error states and an alternative discovery route where useful.
- **SHOULD:** Evaluate whether visitors can find a known item and discover an unfamiliar relevant offering; see section 15 for validation.

Search, large menus and audience segmentation are choices, not mandatory features. Do not require a marketing hero before task entry or content discovery.

## 8. Calls to action, visitor journeys and compliance UI

### 8.1 Calls to action

A CTA is a meaningful next action, including exploring further content.

- **MUST:** Communicate what an action will do.
- **SHOULD:** Make a primary action visually distinguishable when one exists.
- **SHOULD:** Avoid unnecessary competing actions.
- **MUST:** Use understandable accessible names and appropriate link/button semantics.
- **MUST NOT:** Misrepresent cost, eligibility, availability or outcomes.
- **MUST NOT:** Use fabricated scarcity, deceptive countdowns or misleading confirmation.
- **MAY:** Offer different paths for genuinely different audiences.

### 8.2 Privacy, cookie consent and compliance UI

Consent notices, age gates, regional disclaimers and other compliance interfaces have different purposes and legal requirements. Determine the applicable jurisdictions, processing purposes and required user choices **before** selecting a pattern. This guideline is not legal advice and does not declare one jurisdiction's specific interface rules universal.

- **MUST:** Make compliance controls keyboard accessible, readable and operable with appropriate semantics.
- **MUST:** Match focus behavior to the actual interaction: a **modal dialog** restricts interaction with the underlying page and needs appropriate modal semantics and focus management; a **nonmodal notice** must not trap focus or incorrectly claim that the page is modal.
- **MUST:** Fulfill applicable consent and disclosure obligations; do not defer or hide a legally required choice merely to improve the hero's appearance.
- **MUST NOT:** Use deceptive consent patterns such as hidden choices, misleading preselected options or manipulated descriptions of consequences. Check jurisdiction-specific requirements for button presentation and choice equivalence; do not assume identical styling is a universal legal mandate.
- **MUST:** Avoid *unnecessary unexpected* layout shifts when the notice appears or closes, and satisfy the adopted CLS requirements. Reserve space or use a suitable overlay when appropriate; do not require literal zero CLS in every context.
- **SHOULD:** Keep page navigation and important context discoverable where legally permissible, without obscured keyboard focus or unreachable controls.
- **SHOULD:** Minimize data collection to what is necessary for the stated purpose and disclose the use of optional analytics and marketing technologies accurately.

### 8.3 First-time and returning journeys

- **SHOULD:** Determine whether persistent navigation or separate entry routes help first-time visitors learn and returning visitors reach known content, access an existing account or resume a task, where those functions exist.
- **SHOULD:** Keep relevant returning routes discoverable without forcing repeated promotional sequences; retain explanations for visitors who need them.
- **MAY:** Provide explicit choices such as browse, sign in or resume when justified by actual functionality. Personalization, registration and visitor tracking are not required; direct links and consistent navigation may be sufficient.
