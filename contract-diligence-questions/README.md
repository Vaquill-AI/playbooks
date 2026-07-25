# Contract Due-Diligence Question Bank

A vetted, open question bank for contract review and due diligence across common deal types.

Each entry is a plain question paired with an answer type, so it drops cleanly into any contract-review tool, spreadsheet, or LLM extraction pipeline.
There are 8 question sets covering 145 questions in total, spanning M&A, NDAs, commercial leases, employment agreements, SaaS master service agreements, loan agreements, shareholder agreements, and data-processing agreements.

The questions are written to be answerable from the document itself.
They ask you (or a model) to extract what a contract says, not to opine on whether a term is good, fair, or enforceable.

## What is in here

- `questions.json` - all 8 question sets as clean, machine-readable JSON. This is the source of truth.
- `templates/` - one human-readable Markdown table per question set.
- `README.md` - this file.

## Answer types

Every question carries an `column_type` that tells you what shape of answer to expect.
This lets you validate extracted values, drive a form control, or build a spreadsheet column.

| `column_type` | Meaning | Example answer |
|---------------|---------|----------------|
| `free_text` | Open text, usually a short summary | "Delaware law governs; disputes in New York courts." |
| `single_select` | One value from a fixed `options` list | "stock purchase" |
| `date` | A calendar date | "2025-03-14" |
| `money` | A monetary amount | "$4,500,000" |
| `yes_no` | A yes or no answer | "yes" |
| `party_name` | The name of a party or entity | "Acme Holdings, Inc." |

Questions with `column_type: single_select` include an `options` array listing the allowed values.

## Question sets

| Question set | File | Questions | Focus |
|--------------|------|-----------|-------|
| M&A Due Diligence | [templates/ma-diligence.md](templates/ma-diligence.md) | 25 | Parties, structure, price, indemnification, escrow, regulatory, termination |
| NDA Review | [templates/nda-review.md](templates/nda-review.md) | 13 | Parties, term, exclusions, return-or-destroy, equitable relief |
| Commercial Lease Abstraction | [templates/commercial-lease-abstraction.md](templates/commercial-lease-abstraction.md) | 20 | Parties, premises, rent, escalations, renewal, default, casualty |
| Employment Agreement Review | [templates/employment-agreement-review.md](templates/employment-agreement-review.md) | 16 | Compensation, equity, IP assignment, restrictive covenants, termination |
| SaaS MSA Review | [templates/saas-msa-review.md](templates/saas-msa-review.md) | 19 | Fees, term, SLAs, data processing, security, IP ownership, liability |
| Loan Agreement Review | [templates/loan-agreement-review.md](templates/loan-agreement-review.md) | 19 | Principal, interest, repayment, collateral, covenants, defaults, remedies |
| Shareholder Agreement Review | [templates/shareholder-agreement-review.md](templates/shareholder-agreement-review.md) | 15 | Parties, share classes, board, reserved matters, drag/tag-along, exit, deadlock |
| DPA / Sub-processor Review | [templates/dpa-subprocessor-review.md](templates/dpa-subprocessor-review.md) | 18 | Controller/processor roles, data categories, breach notice, transfers, audit |

Total: 8 question sets, 145 questions.

## How to use it

1. Pick the question set that matches your document type and load it from `questions.json`.
2. For each question, pull the relevant text from the contract, either by hand or with a retrieval or extraction tool.
3. Map each answer to its `column_type`. Use the `options` list to constrain `single_select` answers.
4. Keep a pointer back to the source clause for every answer, so a reviewer can verify it.

The JSON is intentionally tool-neutral.
You can feed it to a spreadsheet as column definitions, render it as a review form, or hand each question to a language model as an extraction prompt.
A common pattern is one row per document and one column per question, which turns a stack of contracts into a comparable grid.

## Provenance

These question sets were assembled from common practice-area review checklists and informed by public academic contract datasets, including CUAD and MAUD.
They are meant as a practical starting point that you can extend or trim for your own workflow.

---

General reference, not legal advice. See [../DISCLAIMER.md](../DISCLAIMER.md).

Licensed under [CC BY 4.0](../LICENSE).
