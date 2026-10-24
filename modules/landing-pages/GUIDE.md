# Landing pages — ULPG module

**Module version:** 0.4.0 · **Integration revision:** 1 · **DDM candidate:** 2.4.0

This is the integrated Universal Landing Page Guide (ULPG) v0.4.0. Its twenty numbered sections retain their source wording and MUST/SHOULD/MAY levels. The source has section identifiers, not individual requirement IDs; migration IDs in `traceability.json` identify source lines without pretending they were upstream IDs. See [provenance](PROVENANCE.md) and the retained [license](LICENSE).

## Apply within DDM

Read this entry point only for landing pages, homepages, product introductions, campaign entry points, portfolios, service introductions or editorial entry pages. Unrelated UI work uses DDM alone. Start with [requirement levels and evidence](validation.md), then load the topic files relevant to the requested change. For a new page or broad review, read all five topic files. Each file contains intact numbered sections; cross-references such as “section 6.1” resolve through the table below.

For a narrow change, reuse established audience, entry-pattern and navigation decisions; verify only affected requirements and supported journeys. Record a new rationale when those decisions change. A copy edit does not require a new page brief, object map or full-page audit. This scoping rule selects applicable work; it does not downgrade an applicable MUST. Do not claim unchecked page-wide conformance. Use DDM's existing conditional map gate and decision record; the templates below are optional scaffolds, not additional mandatory documents.

DDM owns the general method, system-selection precedence and object-map gate. This module is the authority for landing-page-specific entry, navigation, communication, trust, demonstrations, maintenance and page evaluation. An adopted Web HIG remains the independent authority for interface behavior and its conformance contract. ULPG's technical measurement contract is retained; satisfy overlapping obligations with the same evidence rather than duplicate implementations or checks. Resolve conflicts using section 17 and DDM's project-context rules; record deviations and never silently weaken binding obligations.

| Sections | Read when | File |
|---|---|---|
| 3, 4, 8 | Context, hierarchy, entry patterns, discovery, journeys, actions or consent UI | [Entry and navigation](entry-and-navigation.md) |
| 5, 7, 9, 14 | Copy, density, identity, evidence, freshness or page-type adaptation | [Content and trust](content-and-trust.md) |
| 6, 10, 11 | Media, demos, accessibility, responsive/localized content or motion | [Interaction and demonstrations](interaction-and-demonstrations.md) |
| 12, 13 | Performance, scripts, field/lab evidence or discoverability | [Technical quality](technical-quality.md) |
| 2, 15–18 | Requirement levels, acceptance, validation, non-regression or conflicts | [Validation](validation.md) |
| 1, 19, 20 | Purpose, principle and glossary | This file |

## Optional working artifacts

Use the [page brief](templates/page-brief.md), [review](templates/review.md), [decision record](templates/decision-record.md), [performance budget](templates/performance-budget.md) or [third-party inventory](templates/third-party-inventory.md) only where useful. Capture the same information inline or in the existing project record when that is sufficient. Read [references and boundaries](references.md) before relying on external claims. The [five source scenarios](examples/entry-pattern-regression.md) and [editorial example](examples/editorial-review.md) are illustrative heuristic documentation reviews, not merged behavioral results.

**Validation status:** Source retention can be checked automatically using `traceability.json`; implemented-page quality and agent behavioral non-regression remain unverified. See the packaged evaluation protocol in `evals/landing-pages/protocol.md` relative to the skill root. The independent ULPG repository has not been retired or changed by this integration.

## 1. Purpose

A landing page should communicate its intended message clearly, help visitors recognize whether its offering or content is relevant, provide sufficient information for an informed decision, and support a meaningful next action.

The next action need not be a purchase or registration. It may be reading, exploring, contacting, comparing, subscribing, downloading or navigating elsewhere.

A successful landing page should be:

1. **Understandable:** Its primary purpose is recognizable quickly.
2. **Relevant:** Its information reflects audience needs and context.
3. **Informative:** It provides enough information to support decisions.
4. **Credible:** Claims are accurate and evidence is appropriately presented.
5. **Navigable:** Users can find information and move without confusion.
6. **Accessible:** The experience works across abilities and input methods.
7. **Responsive:** Information and functionality adapt to devices.
8. **Performant:** It loads and responds efficiently.
9. **Visually coherent:** The presentation reinforces its purpose and brand.
10. **Measurable:** Relevant outcomes can be evaluated without inventing results.

The objective is not maximum visual appeal, minimum page length or maximum conversion at any cost.

**Guiding objective:** The simplest effective presentation that communicates the required information without compromising comprehension, accessibility, trust or usability.

## 19. Guiding principle

**A modern landing page should reveal the right information, at the right level of detail, in the most understandable form, when visitors need it.**

It should be appropriate without decorative excess, concise without withholding necessary information, persuasive without misleading, and technically modern without sacrificing usability. Evaluate against intended users and purpose—not a universal page template.

## 20. Glossary

- **Above the fold:** The portion of a page visible before scrolling, dependent on viewport and settings.
- **Cumulative Layout Shift (CLS):** A Core Web Vitals metric of unexpected visual layout shifts over a page visit, using a defined session-window aggregation.
- **Deceptive pattern:** An interface that misleads or manipulates people into decisions they might not otherwise choose.
- **Interaction to Next Paint (INP):** A Core Web Vitals responsiveness metric based on high-latency interactions over the visit, with adjustment for pages containing many interactions; not a simple sum of every interaction delay.
- **Largest Contentful Paint (LCP):** A loading-performance metric indicating when the largest qualifying visible content element renders.
- **Modal dialog:** A dialog that makes underlying content temporarily unavailable for interaction and therefore requires suitable semantics and focus handling.
- **Nonmodal notice:** A notice that does not prevent interaction with the underlying page and should not trap focus as if modal.
- **Progressive disclosure:** Revealing advanced or secondary information when relevant while keeping essential information available.
- **Semantic tokens:** Design tokens named for their role, such as `surface-primary` or `action-danger`, instead of a raw visual value.
