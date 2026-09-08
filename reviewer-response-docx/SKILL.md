---
name: reviewer-response-docx
description: Revise a scientific manuscript and create an auditable point-by-point response package in Word using blue reviewer comments, black responses, red italic revised excerpts, verified locations, clean, marked, and tracked manuscripts, and explicit pending-item labels. Use for 审稿意见回复, 返修, response to reviewers, rebuttal, revision letters, or manuscript revision packages. Do not use for peer-review reports written by a reviewer about someone else's paper.
---

# Reviewer Response DOCX

Produce a scientifically honest revision package whose response, manuscript, supplement, references, figures, and change locations agree.

## Required intake

Inspect all supplied materials before drafting: the editor decision and decision type; complete reviewer reports; manuscript, supplement, figures, tables, data, and code; previous revision files that define the requested format; and current journal instructions when relevant. If the decision is not explicit, ask whether it is major or minor revision. Never infer it from comment tone or count.

## Working method

1. Preserve every editor and reviewer comment verbatim. Assign stable internal IDs, but use neutral `Comment 1` labels in reviewer-facing files.
2. Build an internal tracker before prose. Record the concern, evidence required, action, status, destination, location, and whether each item blocks submission.
3. Search primary literature when a comment needs evidence. Verify title, authors, year, journal, pages, and DOI. Distinguish literature context from analyses actually performed.
4. Inspect the complete paragraph before editing. Prefer replacement or compression over defensive additions. Put non-central robustness and implementation detail in the supplement.
5. Never invent results, experiments, citations, figure changes, line numbers, or validation. Use `AUTHOR_INPUT_NEEDED` or `DEFERRED_BY_AUTHOR` when work remains.
6. Treat reviewer reports as mutually blind unless the journal explicitly requires a combined visible response. A reviewer-specific file contains only that reviewer's material.
7. When a reviewer missed existing material, improve its visibility or wording. Do not rebuke the reviewer by saying it was already clear.
8. For disagreement, acknowledge the concern, present evidence, narrow the claim where needed, and state the exact manuscript action.

## Use comments as diagnosis, not manuscript dictation

Treat each reviewer comment as evidence of an underlying scientific, evidential, interpretive, or presentation problem. Identify that problem first, then revise the paper around the study's own argument and the needs of future readers. The response letter answers the reviewer directly; the manuscript should read as a coherent paper that would make sense without the review history.

- Do not mechanically transplant the reviewer's wording, requested list, question order, or rebuttal logic into the manuscript.
- Do not add sentences whose main purpose is to announce compliance, defend the authors, or answer a reviewer in disguise.
- Integrate the valid concern into the existing argument by revising the claim, evidence chain, explanation, method, limitation, or transition that caused the concern.
- Use relevant literature to establish the scientific basis, boundary, or competing interpretation. Cite sources because they support the revised argument, not merely because the reviewer requested more citations.
- Synthesize multiple sources and the study's own evidence. Avoid a one-comment-to-one-sentence pattern when the concern is better resolved by restructuring or replacing a paragraph.
- Preserve the author's analytical judgment. If the literal requested wording would overstate evidence, distort scope, duplicate content, or disrupt the paper, solve the underlying concern through a better-supported revision and explain that choice respectfully in the response.
- Direct corrections remain appropriate for factual errors, missing definitions, reproducibility details, reporting requirements, and reader-critical limitations. This principle does not justify evading a valid request or hiding a limitation.

Before accepting a manuscript edit, apply this test: if all reviewer labels and correspondence disappeared, would the passage still be necessary, evidence-based, naturally placed, and useful to the paper's readers? If not, keep the fuller explanation in the response letter and revise the manuscript more economically.

## Response anatomy

For every completed comment use: verbatim reviewer comment; bold `Response`; a direct evidence-linked answer; bold red `Revision`; a bold location such as `(Section 3.2; Manuscript, pp. 8–9, paragraph 68)`; and the verbatim revised manuscript excerpt in red italics. The response must stand alone without referring to another reviewer.

For a pending item, reproduce the comment and add a visible red `AUTHOR WORKING NOTE — DEFERRED` or `AUTHOR_INPUT_NEEDED`. Do not imply completion. Mark the package as a working draft.

## Word house style

Read [references/word-format.md](references/word-format.md) before creating or editing response documents. Use [assets/response-template.docx](assets/response-template.docx) when starting a new response.

Create, when supported by the inputs: a combined response; separate reviewer files; clean, red-marked, and native tracked-changes manuscripts; equivalent supplement variants; a concise cover letter; and an internal change-location and evidence log.

## Verification gate

Run [scripts/validate_response_docx.py](scripts/validate_response_docx.py) on the response. Run [scripts/compare_docx_packages.py](scripts/compare_docx_packages.py) when clean, marked, and tracked manuscripts exist.

Verify that every comment has one response or explicit pending label; completion claims match inspectable work; every excerpt occurs verbatim in the clean manuscript; page locations come from the final rendered clean Word file and include stable section or paragraph identifiers; clean and marked accepted text is identical; accepted tracked text equals clean text; current-round red marks use the correct baseline; equations, tables, captions, units, abbreviations, references, and figures agree; reviewer-specific files reveal no other reviewer; and unresolved work is visible.

Also conduct a reader-facing revision audit. Remove reviewer-dependent phrases, compliance language, question-and-answer residue, unnecessary repetition, and citations added without a substantive role. Confirm that every changed paragraph has a clear function in the paper independent of the review exchange.

Return `ready_to_submit` only when no blocking or deferred item remains. Otherwise return `draft_with_placeholders`, `needs_author_input`, or `working_draft_with_deferred_items` prominently.
