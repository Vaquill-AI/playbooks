# US Residential Landlord-Tenant Rules Database

A cited, machine-readable reference of US residential landlord-tenant statutory rules across all 50 states plus the District of Columbia.

Each table is a JSON file keyed by 2-letter USPS state code.
Every cell keeps the controlling statute citation (for example `A.R.S. § 33-1368(B)`).
The data covers the deadlines and caps that most often decide a residential tenancy dispute: security deposits, eviction notice and cure periods, just-cause regimes, entry notice, late fees, retaliation windows, disclosures, and rent increases.

## Not legal advice, and verify against current statute

This is a general reference, not legal advice, and it does not create an attorney-client relationship.
Landlord-tenant law changes every year and varies by state, county, and city.
Section numbers move, caps get re-indexed, and new statutes supersede old ones.
Do not rely on any figure here without confirming it against the current official state code and any applicable local ordinance.

These tables were last reviewed against the state codes in **2026-05**.
CPI-indexed figures (some rent-increase caps and the screening-fee cap) change on a fixed annual cadence, so treat any dated or indexed value as provisional and re-verify the current-year number.

## Tables

Each file lives in `data/` and carries its own `_notice`, `_last_reviewed`, and per-table `_note` metadata alongside the state entries.

| File | Description |
| --- | --- |
| `data/security-deposit-caps.json` | Maximum security deposit a landlord may collect, in months of rent (`null` where no statewide cap). |
| `data/security-deposit-return-windows.json` | Deadline, in days after move-out, to return the deposit or deliver an itemized claim. |
| `data/security-deposit-interest.json` | States that statutorily require interest to be paid on residential security deposits. |
| `data/notice-to-pay-or-quit-cure.json` | Cure period for nonpayment before an eviction may proceed, with the day-count basis. |
| `data/notice-to-cure-or-quit.json` | Cure period for a non-monetary lease breach, with the day-count basis. |
| `data/statewide-just-cause.json` | States with a statewide just-cause (for-cause) eviction regime. |
| `data/local-just-cause.json` | City and county just-cause ordinances that overlay state law (keyed by city or county name, not state code). |
| `data/month-to-month-termination-landlord.json` | Landlord no-cause notice period to end a month-to-month tenancy, plus any long-tenancy or just-cause special rule. |
| `data/month-to-month-termination-tenant.json` | Tenant notice period to end a month-to-month tenancy. |
| `data/entry-notice.json` | Advance notice a landlord must give before non-emergency entry. |
| `data/late-fee-rules.json` | States that statutorily cap or regulate late fees. |
| `data/retaliation-presumption-windows.json` | Window, in days after protected tenant activity, during which retaliation is presumed. |
| `data/source-of-income-protection.json` | States that protect lawful source of income, including Section 8 / Housing Choice Vouchers. |
| `data/unconditional-quit-grounds.json` | Statutory grounds that permit an unconditional notice to quit with no cure right. |
| `data/service-of-notice.json` | Statutorily authorized methods for serving a pre-suit landlord-tenant notice. |
| `data/lead-paint-disclosure.json` | State lead-paint disclosure duties beyond the federal pre-1978 rule. |
| `data/bed-bug-disclosure.json` | State bed bug disclosure and treatment duties. |
| `data/mold-disclosure.json` | State mold disclosure and remediation duties. |
| `data/rent-increase-rules.json` | Rent-increase cap and the notice periods that gate it. |
| `data/key-rules.json` | Extra high-frequency reference facts (repair-and-deduct limits, illegal-lockout penalties, and similar), one list per state. |

## Schema

Every file is a JSON object.
Underscore-prefixed top-level keys (`_table`, `_key`, `_note`, `_last_reviewed`, `_notice`, `_entries`) hold metadata.
All other top-level keys are 2-letter USPS state codes (or, for `local-just-cause.json`, lowercased city or county names).

Cell shapes by table type:

- Security deposit caps: `{ "months": 1.0 | null, "citation": "..." }`
- Deposit return windows, tenant month-to-month, retaliation windows: `{ "days": 30, "citation": "..." }`
- Pay-or-quit and cure-or-quit periods: `{ "days": 3, "basis": "calendar" | "weekday" | "hours" | "n/a", "citation": "..." }` where `days` is `0` when there is no statutory pre-suit cure window.
- Landlord month-to-month: `{ "days": 30, "citation": "...", "special_rule": "..." | null }`
- Entry notice: `{ "notice": "24 hours", "citation": "..." }`
- Narrative tables (statewide/local just-cause, deposit interest, late fees, source-of-income, unconditional-quit grounds, service of notice, all three disclosure tables): a single descriptive field (`rule`, `ordinance`, `grounds`, or `method`) whose text carries the controlling citation inline.
- Rent-increase rules: `{ "cap_summary": "...", "cap_citation": "..." | null, "notice_under_threshold": "...", "notice_over_threshold": "..." | null, "notice_citation": "..." | null }`
- Key rules: a list of `{ "category": "...", "value": "...", "detail": "..." | null, "citation": "..." | null, "volatile": false, "effective_through": "2026-12-31" | null }`

## Coverage

The core tables (deposit caps and return windows, pay-or-quit and cure-or-quit periods, both month-to-month termination tables, entry notice, and service of notice) cover all 51 jurisdictions (50 states plus DC).
The remaining tables are intentionally partial: a state appears only where a statute actually asserts the rule, so an absent state means "no statewide rule asserted here" rather than a guessed default.

## Rebuilding

`build.py` regenerates every file in `data/`.
It reads the source data tables statically and writes only inside this folder.

## License

Licensed under [CC BY 4.0](../LICENSE).

---

General reference, not legal advice. Statutes change; verify against the current official code. Last reviewed 2026-05. See [../DISCLAIMER.md](../DISCLAIMER.md).

Licensed under [CC BY 4.0](../LICENSE).
