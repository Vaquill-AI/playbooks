# US Commercial Contract Clause Library

A curated, open library of neutral exemplar clauses for United States commercial contracts.
It contains 46 professionally drafted clauses across 24 clause types.
Every clause is a synthetic exemplar written to illustrate a common negotiating position, not a clause copied from any real agreement.
Each clause is tagged with its drafting tone, the statutes or authorities it engages, and the contract types it fits.

## What this is

This library is a starting point for drafting, review, and contract-technology work.
The clauses cover the operative and boilerplate provisions that recur across SaaS agreements, master services agreements, statements of work, vendor and procurement contracts, NDAs, licenses, and employment agreements.
Clauses are drafted at three tones so you can pick a starting posture and negotiate from there.

- `permissive`: lighter obligations, often favorable to the receiving or paying party.
- `balanced`: a mutual, middle-of-the-road position suitable as a neutral first draft.
- `protective`: stronger safeguards, often favorable to the disclosing or providing party.

## Clause types

| Clause type | Count | Tones | File |
| --- | --- | --- | --- |
| Limitation of Liability | 3 | permissive, balanced, protective | [clauses/limitation-of-liability.md](clauses/limitation-of-liability.md) |
| Indemnification | 4 | permissive, balanced, protective | [clauses/indemnification.md](clauses/indemnification.md) |
| Confidentiality | 3 | permissive, balanced, protective | [clauses/confidentiality.md](clauses/confidentiality.md) |
| Termination | 3 | balanced, protective | [clauses/termination.md](clauses/termination.md) |
| Governing Law | 2 | balanced | [clauses/governing-law.md](clauses/governing-law.md) |
| Dispute Resolution | 3 | balanced, protective | [clauses/dispute-resolution.md](clauses/dispute-resolution.md) |
| Intellectual Property | 3 | permissive, balanced | [clauses/intellectual-property.md](clauses/intellectual-property.md) |
| Data Protection | 4 | balanced, protective | [clauses/data-protection.md](clauses/data-protection.md) |
| Payment Terms | 2 | balanced, protective | [clauses/payment-terms.md](clauses/payment-terms.md) |
| Representations and Warranties | 1 | balanced | [clauses/representations-warranties.md](clauses/representations-warranties.md) |
| Assignment | 1 | balanced | [clauses/assignment.md](clauses/assignment.md) |
| Insurance | 1 | balanced | [clauses/insurance.md](clauses/insurance.md) |
| Non-Solicitation | 1 | balanced | [clauses/non-solicitation.md](clauses/non-solicitation.md) |
| Non-Compete | 2 | balanced | [clauses/non-compete.md](clauses/non-compete.md) |
| Force Majeure | 1 | balanced | [clauses/force-majeure.md](clauses/force-majeure.md) |
| Audit Rights | 1 | balanced | [clauses/audit-rights.md](clauses/audit-rights.md) |
| Entire Agreement | 1 | balanced | [clauses/entire-agreement.md](clauses/entire-agreement.md) |
| Severability | 1 | balanced | [clauses/severability.md](clauses/severability.md) |
| Waiver | 1 | balanced | [clauses/waiver.md](clauses/waiver.md) |
| Notices | 1 | balanced | [clauses/notices.md](clauses/notices.md) |
| Survival | 1 | balanced | [clauses/survival.md](clauses/survival.md) |
| Amendment | 1 | balanced | [clauses/amendment.md](clauses/amendment.md) |
| Subcontracting | 1 | balanced | [clauses/subcontracting.md](clauses/subcontracting.md) |
| Custom and Specialty Clauses | 4 | balanced, protective | [clauses/custom.md](clauses/custom.md) |
| **Total** | **46** | | |

## Schema

`clauses.json` is a JSON array of clause objects.
Each object has the following fields.

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Human-readable title summarizing the clause and its key features. |
| `clause_type` | string | The clause category, for example `limitation_of_liability`. |
| `tone` | string | One of `permissive`, `balanced`, or `protective`. |
| `jurisdiction` | string | Always `US` for this library. |
| `content` | string | The full clause text, with paragraph breaks encoded as newlines. |
| `applicable_acts` | string[] | Statutes, regulations, or standards the clause engages. May be empty for general boilerplate. |
| `tags` | string[] | Descriptive keywords for search and filtering. |
| `applicable_categories` | string[] | Contract types the clause commonly appears in, for example `saas`, `msa`, `nda`. |

### Example record

```json
{
  "name": "Limitation of Liability (mutual, 12-month fee cap, consequential waiver with carve-outs)",
  "clause_type": "limitation_of_liability",
  "tone": "balanced",
  "jurisdiction": "US",
  "content": "(a) Exclusion of Indirect Damages. Except as provided in subsection (c), neither party will be liable to the other for any indirect, incidental, special, consequential, exemplary,  ...",
  "applicable_acts": [
    "Uniform Commercial Code § 2-719",
    "Cal. Civ. Code § 1668"
  ],
  "tags": [
    "limitation-of-liability",
    "liability-cap",
    "consequential-damages-waiver",
    "mutual",
    "..."
  ],
  "applicable_categories": [
    "saas",
    "msa",
    "vendor_agreement",
    "..."
  ]
}
```

## Suggested uses

- **Drafting starter.** Pull a clause of the right type and tone, then adapt the defined terms, cure periods, caps, and jurisdiction to your deal.
- **RAG or fine-tuning demo corpus.** The dataset is small, clean, and consistently structured, which makes it a convenient corpus for retrieval-augmented generation demos, embeddings experiments, and instruction-tuning examples over legal text.
- **Contract-technology reference.** Use the clause types, tones, tags, and category mappings as a taxonomy for clause classifiers, playbook builders, and clause-comparison tools.
- **Negotiation training.** Compare the permissive, balanced, and protective versions of the same clause type to study how risk allocation shifts between parties.

## Coverage notes

- All clauses are drafted for United States commercial contracts and reference United States federal and state law.
- Some data-protection clauses also incorporate cross-border transfer terms, such as the EU Standard Contractual Clauses, because United States vendors routinely process data originating outside the United States.
- Restrictive-covenant clauses, such as non-compete and non-solicitation, include state-law savings language because enforceability varies widely by state and several states void post-employment non-competes.
- Bracketed placeholders such as `[STATE]` and `[COUNTY/CITY]` mark terms you must complete before use.

## Important disclaimer

These are neutral exemplar clauses meant to be adapted.
They are not legal advice and do not create an attorney-client relationship.
Enforceability of any clause depends on the governing law, the parties, and the specific transaction.
Always have qualified counsel tailor any clause to your deal and jurisdiction before use.

## License

This clause library is released under the Creative Commons Attribution 4.0 International license.

---

Neutral exemplar clauses for adaptation, not legal advice.
Have counsel tailor any clause to your deal and jurisdiction.
See [../DISCLAIMER.md](../DISCLAIMER.md).

Licensed under [CC BY 4.0](../LICENSE).
