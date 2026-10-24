# Technical quality

Read [module scope and section routing](GUIDE.md) first. Numbered sections below retain ULPG v0.4.0 wording.

## 12. Performance and technical quality

### 12.1 Core Web Vitals

A modern landing page should prioritize meaningful content availability, responsiveness and stability. Use the [Core Web Vitals good-experience reference thresholds](https://web.dev/articles/vitals) at the 75th percentile of visits, segmented by mobile and desktop:

| Metric | Good threshold |
|---|---|
| Largest Contentful Paint (LCP) | ≤ 2.5 seconds |
| Interaction to Next Paint (INP) | ≤ 200 milliseconds |
| Cumulative Layout Shift (CLS) | ≤ 0.1 |

- **MUST:** Preserve stricter targets imposed by the adopting project.
- **SHOULD:** Avoid unnecessary JavaScript, oversized imagery, blocking resources and unexpected layout shifts.
- **SHOULD:** Provide functional content before nonessential enhancement loads.
- **MUST NOT:** Claim field performance based solely on laboratory testing.
- **SHOULD:** Assess real-user performance with field data when available, documenting its page/origin scope, collection window and device segmentation. Use laboratory tests for diagnosis and regression detection; if field evidence is unavailable, mark field outcomes unverified. A Lighthouse score or visual appearance does not establish real-user performance. See [Google's field/lab explanation](https://developers.google.com/speed/docs/insights/v5/about).

### 12.2 Third-party scripts and analytics governance

Analytics, tag managers, marketing pixels, chat widgets and other third-party code may affect user experience, security and privacy. Cumulative execution time alone does not describe third-party blocking impact; no universal **250 ms MUST** applies.

- **MUST:** Identify and document third-party scripts, their purpose, owner, necessity, data processing and performance/security implications.
- **MUST:** Respect applicable consent and data-processing requirements before loading or activating optional scripts where consent is required.
- **SHOULD:** Define **project-specific, measurable** third-party performance budgets with documented devices, network conditions, time windows, attribution method and pass/fail rules. Evaluate impact on INP, LCP, CLS and main-thread responsiveness where relevant.
- **SHOULD:** Defer noncritical scripts when doing so does not break required functionality, consent handling or justified measurement needs. `requestIdleCallback` and post-LCP loading are options, not universal prescriptions.
- **SHOULD:** Prevent third-party popups and widgets from unexpectedly shifting content, blocking essential actions or stealing focus.
- **SHOULD:** Review the third-party inventory periodically, on a cadence appropriate to project risk; quarterly is one optional operational schedule, not a universal MUST.
- **MAY:** Include a **250 ms diagnostic budget** in a project-specific experiment if the metric, measurement procedure and rationale are explicitly defined. Do not present it as a Core Web Vitals threshold or a universal total script-execution limit.

## 13. SEO and content discoverability

Where search discovery is relevant:

- **SHOULD:** Provide a descriptive title and useful metadata.
- **SHOULD:** Use appropriate semantic heading structure.
- **SHOULD:** Keep important content accessible in crawlable document content.
- **SHOULD:** Use canonical URLs and relevant structured data where warranted.
- **MUST NOT:** Add misleading structured data or unsupported claims.
- **MAY:** Develop dedicated pages for distinct topics or search intent.

Search optimization must not reduce comprehension or create repetitive content.
