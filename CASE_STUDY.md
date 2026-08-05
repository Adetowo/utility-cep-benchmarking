# Case Study: Supplier Diversity Program Benchmarking

> Client and figures generalized to protect confidentiality. Methodology and approach are as delivered.

## Situation

A large public utility's supplier/contract equity program needed an evidence-based answer to a question leadership kept asking informally: *how does our program actually compare to peers, and what specifically should we fix?* No consistent framework existed to answer it — peer programs publish data in different formats, at different levels of detail, on different timelines.

## Task

Design and execute a comparative benchmarking analysis against 8 peer organizations (investor-owned utilities, public water authorities, and a state transportation agency) that would:
- Produce a defensible, evidence-based score for the program and every peer
- Identify specifically where the program was strong vs. lagging
- Translate gaps into prioritized, peer-sourced recommendations leadership could act on

## Action

- Designed a **5-dimension, 33-indicator evaluation rubric** (Design & Structure, Implementation & Operations, Outreach & Accessibility, Program Outcomes, Economic & Community Impact) grounded in what a mature program should demonstrably do.
- Defined a **4-point evidence standard** (0 = not present → 3 = best-in-class) so scoring stayed consistent and auditable across 9 organizations and hundreds of individual scoring decisions.
- Sourced evidence **exclusively from public documentation** (annual reports, regulatory filings, supplier portals, economic impact studies) so every score could be traced back to a citation.
- Built a **normalization method** — `(raw score / max possible) × 5` — so dimensions with different numbers of indicators (4 vs. 9) could be compared fairly, both peer-to-peer and against a peer-average baseline.
- Ran **two comparison lenses**: individual one-to-one peer comparisons (what does this specific peer do well?) and an aggregate peer-average benchmark (where does the program sit relative to the whole cohort?).
- Converted each identified gap into a **peer-sourced recommendation** — every recommendation named which peer(s) demonstrated the practice, so it wasn't a hypothetical suggestion but a proven one.

## Result

- Delivered a full comparative report identifying the program's largest gap (a 2.45-point shortfall on a 5-point scale in one dimension) against the peer average, with the other two priority gaps quantified and root-caused.
- Recommendations were explicitly staffing- and practice-specific (e.g., "expand from 2–3 FTE to include a dedicated data analyst and outreach specialist role") rather than generic, because they were built from what specific, named peers actually do.
- Framework is reusable: the scoring engine (see `scripts/normalize_scores.py` in this repo) can be pointed at any indicator-level CSV to re-run the same normalization and comparison logic on a different program or a future year's data.

## Why This Translates to Data / AI Transformation Work

This project is, structurally, a rubric-based evaluation problem: define measurable criteria, score against a consistent standard, normalize across uneven categories, and turn the output into a ranked, actionable gap analysis. That's the same core pattern behind:
- AI model / output evaluation rubrics
- Vendor and tooling comparisons in an AI transformation roadmap
- Data quality and program maturity scorecards
- Any "how do we compare, and what do we fix first" question that shows up constantly in transformation and analytics work

## Tools

Excel (scoring matrix, original delivery format) · Python / pandas (scoring engine, reproducible in this repo) · matplotlib (visualization) · Word (executive reporting)
