# Validation

Read [module scope and section routing](GUIDE.md) first. Numbered sections below retain ULPG v0.4.0 wording.

## Retained DDM evaluation refinements

The page-specific checks in section 15 are authoritative; these optional DDM study techniques supply additional detail. A brief exposure followed by audience, offer and next-step questions can explore initial comprehension. A five-second test is one optional method, not a universal duration or acceptance threshold; follow with deeper questions where needed. First-click observation can help investigate discovery, but a visible link alone does not establish successful finding. Factual claim review and perceived trust are different observations. More signups or clicks do not establish that visitors understood material conditions before choosing.

Where activation is part of the real product, walk the actual route into signup, onboarding or the first useful task, including handoff and recovery. A mockup shows only a proposed route. Activation, conversion and retention need analytics or appropriate research; record measurement scope, period and limitations. Report comprehension and task results only when participants were actually observed. Aesthetics cannot establish those outcomes.

## 2. Requirement levels

- **MUST:** A foundational requirement necessary for this guideline's intended quality baseline.
- **SHOULD:** A strong recommendation that may be adapted when justified by the experience.
- **MAY:** An optional technique that can improve a particular experience.

These keywords express *this guideline's* requirements. They do not imply that all requirements are mandated by WCAG, Web HIG, browsers or another external standard.

For every requirement assessed, record an **outcome** (pass, fail, not applicable, or unverified) separately from the **validation method**: **proposed**, **heuristically reviewed**, **automatically checked**, **manually tested**, or **user-research validated**. Record the scope, evidence, conditions, and limitations. A proposed change is unverified until evaluated; using one validation method does not establish outcomes outside its scope.

**MUST NOT:** Claim a test result that has not been established. An untested item is **unverified**, not passed.

## 15. Validation and quality assurance

### 15.1 Before implementation

Confirm audience and purpose, hierarchy, evidence, existing design system, applicable requirements and documented trade-offs.

Record the entry-pattern rationale (section 4.5), discovery/navigation choices (section 4.6) and first-time/returning needs (sections 3 and 8.3). Define relevant find, explore and resume tasks; do not invent a returning-user feature merely to complete a checklist.

### 15.2 During implementation

Check semantics, responsive behavior, loading/error fallback where relevant, media optimization, focus, motion preferences, consent interface behavior, localized text and SEO metadata.

For demonstrations, check capability/data labels, static or equivalent fallbacks, keyboard operation and truthful execution feedback with enhancements working, loading and unavailable. Record checks actually performed and remaining gaps.

### 15.3 After implementation

Use purpose-specific evaluation:

| Evaluation | Question |
|---|---|
| First-impression comprehension | Can visitors understand the page's purpose? |
| Relevance | Can the target audience identify suitability? |
| Information discovery | Can visitors locate decision-critical details? |
| First-click testing | Can visitors identify how to proceed? |
| Trust | Are material claims supported? |
| Accessibility | Are applicable requirements met with relevant assistive technologies? |
| Performance | Does the page meet measured budgets and relevant Core Web Vitals thresholds? |
| Consent/localization | Are relevant interaction modes and supported locales functional? |
| Conversion | Does the intended journey perform as measured? |

Define business-specific conversion and comprehension thresholds rather than inventing universal figures. Record what was actually tested and untested.

### 15.4 Ongoing maintenance

Review changing content using section 9.1's ownership and triggers. Recheck offers, prices, feature descriptions, screenshots, availability, links and demonstrations after relevant changes. Record what was verified, when, against which source, and who will resolve stale or unverified information. No fixed review cadence or new tracking requirement follows from this guide.

## 16. Non-regression policy

When improving an existing landing page, **MUST NOT**:

- Remove critical information without an equivalent accessible alternative.
- Break existing routes or supported journeys.
- Weaken accessibility requirements, security or privacy behavior.
- Degrade performance beyond approved project budgets.
- Replace a coherent identity without authorization.
- Remove required product limitations or transaction information.
- Present proposed or experimental functionality as already available.

**SHOULD:** Compare baseline and candidate pages, preserve functionality and SEO-relevant routes, evaluate comprehension and usability, and record justified trade-offs and unresolved limitations.

## 17. Relationship to DDM and Web HIG

### 17.1 Functional boundaries

This guideline is compatible with both projects while remaining independent.

- **DDM determines:** Audience, purpose, information priorities, visual-system selection, relevant user-recognizable objects and relationships, project-specific rationale, and acceptance criteria.
- **Web HIG governs:** Applicable interface behavior, accessibility, semantic implementation, performance, motion, interaction states and its conformance contract.
- **ULPG contributes:** Communication principles, content prioritization, evidence placement, page-type adaptations and journey evaluation.

### 17.2 Contextual conflict resolution

Do **not** apply a fixed ranking that automatically places generic landing-page guidance above DDM, an established brand or an explicit project brief.

1. Identify **binding obligations** first: applicable law, security/safety constraints, accessibility obligations and supported-platform requirements. Their exact scope depends on jurisdiction and deployment; a recommendation should not be presented as statute.
2. Check the **approved project brief**, the existing design system, supported users and the consequences of error. Resolve competing nonbinding recommendations according to these circumstances.
3. Apply **DDM** to document consequential design decisions and relevant source adaptations. Apply **Web HIG** where adopted to the applicable archetype/surface and technical quality contract.
4. Apply **ULPG** as specialized landing-page guidance only where compatible with the foregoing. When guidance conflicts, choose the least complex compliant outcome that preserves comprehension, user control and necessary information.
5. **MUST:** Record unresolved conflicts and deliberate deviations, including the source requirement, proposed adaptation, rationale, testing and responsible reviewer. **MUST NOT:** Silently lower accessibility, security or explicit contractual requirements.

DDM is not a lower-priority category of business preference; it is a **decision method**. Web HIG is not automatically universal law; it is the interface standard when adopted. ULPG does not supersede either.

## 18. Design acceptance checklist

Mark each item **pass, fail, not applicable or unverified**, with evidence where available.

- [ ] Audience and purpose are clear.
- [ ] Essential information follows a meaningful hierarchy.
- [ ] The initial viewport communicates the subject, offering or task; the entry pattern is justified by intent, familiarity and purpose.
- [ ] Discovery and navigation support relevant known-item and exploration tasks across entry routes.
- [ ] First-time and returning needs have been considered, with separate routes only where justified.
- [ ] Below-the-fold content adds useful information.
- [ ] Text and visuals have a purpose.
- [ ] Visual system and brand are consistent with approved requirements.
- [ ] Typography, contrast and interaction are accessible.
- [ ] Material claims are accurate and supported.
- [ ] Changing content has an appropriate maintenance owner and review triggers or cadence.
- [ ] Next actions are discoverable and understandable.
- [ ] Consent/compliance UI uses the correct modal or nonmodal pattern; applicable legal requirements, keyboard behavior and page stability are addressed.
- [ ] Primary content and actions remain usable without animation.
- [ ] Demonstrations, where used, explain capabilities truthfully, label simulated data/actions, and provide meaningful fallbacks and relevant states.
- [ ] Responsive layouts and supported localized content preserve meaning and functionality; no universal 40% test is required.
- [ ] Performance is evaluated against adopted Core Web Vitals and **project-defined** third-party budgets; no universal 250 ms cap is imposed.
- [ ] Third-party scripts, purposes and applicable consent dependencies are documented.
- [ ] SEO essentials are addressed where applicable.
- [ ] Relevant comprehension and usability tests have been considered/performed.
- [ ] Untested items and limitations are disclosed.
- [ ] Existing supported behavior has not regressed.
