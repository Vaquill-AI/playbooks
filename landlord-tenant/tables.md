# Tables overview

Twenty tables, each a JSON file in `data/`.
Nineteen are keyed by 2-letter USPS state code; `local-just-cause.json` is keyed by city or county name.
Every cell keeps its controlling statute citation.

## Security deposits

- [security-deposit-caps.json](data/security-deposit-caps.json): maximum deposit in months of rent (`null` = no statewide cap).
- [security-deposit-return-windows.json](data/security-deposit-return-windows.json): days after move-out to return the deposit or send an itemized claim.
- [security-deposit-interest.json](data/security-deposit-interest.json): states that require interest on the deposit.

## Eviction notices and cure periods

- [notice-to-pay-or-quit-cure.json](data/notice-to-pay-or-quit-cure.json): cure period for nonpayment, with day-count basis.
- [notice-to-cure-or-quit.json](data/notice-to-cure-or-quit.json): cure period for a non-monetary breach, with day-count basis.
- [unconditional-quit-grounds.json](data/unconditional-quit-grounds.json): statutory grounds for an unconditional (no-cure) notice to quit.
- [service-of-notice.json](data/service-of-notice.json): authorized methods for serving a pre-suit notice.

## Termination and just cause

- [statewide-just-cause.json](data/statewide-just-cause.json): states with a statewide just-cause regime.
- [local-just-cause.json](data/local-just-cause.json): city and county just-cause ordinances (keyed by locality name).
- [month-to-month-termination-landlord.json](data/month-to-month-termination-landlord.json): landlord no-cause notice period, plus special rules.
- [month-to-month-termination-tenant.json](data/month-to-month-termination-tenant.json): tenant notice period.

## Ongoing tenancy

- [entry-notice.json](data/entry-notice.json): advance notice before non-emergency entry.
- [late-fee-rules.json](data/late-fee-rules.json): states that cap or regulate late fees.
- [retaliation-presumption-windows.json](data/retaliation-presumption-windows.json): days after protected activity that retaliation is presumed.
- [source-of-income-protection.json](data/source-of-income-protection.json): states protecting lawful source of income and vouchers.
- [rent-increase-rules.json](data/rent-increase-rules.json): rent-increase cap and gating notice periods.
- [key-rules.json](data/key-rules.json): extra reference facts (repair-and-deduct, illegal-lockout penalties, and more).

## Disclosures

- [lead-paint-disclosure.json](data/lead-paint-disclosure.json): state lead-paint duties beyond the federal pre-1978 rule.
- [bed-bug-disclosure.json](data/bed-bug-disclosure.json): state bed bug disclosure and treatment duties.
- [mold-disclosure.json](data/mold-disclosure.json): state mold disclosure and remediation duties.

---

General reference, not legal advice. Statutes change; verify against the current official code. Last reviewed 2026-05. See [DISCLAIMER.md](../DISCLAIMER.md).
