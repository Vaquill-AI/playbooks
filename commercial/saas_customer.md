# SaaS - Customer side

> You're buying SaaS from a vendor. Tightens liability cap protections, secures IP and data-breach indemnities, locks down auto-renewal and data-portability rights, and demands proper sub-processor controls.

**Side:** Customer · **Jurisdiction:** US

**Best fit for:**

- Subscribing to a SaaS product as the buyer
- Vendor-presented order forms / MSAs
- Annual or multi-year cloud-software contracts

**Tags:** `saas`, `customer`, `b2b`, `subscription`

_General US-commercial reference, not legal advice. Verify anything jurisdiction-specific with counsel._

33 clauses.

---

### Limitation of liability

**Preferred position**

Three-tier structure. (1) General cap: mutual, at 24 months of fees (12-month floor) for ordinary claims. (2) SUPER-CAP ('enhanced cap'): 3x-5x fees, or a fixed amount tied to the vendor's cyber-insurance limit, for the vendor's data-breach / security-incident and confidentiality liability. (3) UNCAPPED: the vendor's IP-infringement indemnity, fraud, willful misconduct, and gross negligence (drafted as a finding of fact, not a pleading standard). Only INDIRECT / consequential / incidental / special / punitive damages are waived -- DIRECT damages remain fully recoverable. Cap measured on trailing 12 months of fees PAID (not the lesser of paid-or-due).

**Acceptable range**

General cap 12-24 months. Data-breach / security and confidentiality under a super-cap of 2x-5x fees (target a dedicated data-breach super-cap where data volume is high). IP indemnity uncapped. Mutual general cap only if the vendor delivers a security/privacy uplift (SOC 2 Type II + cyber insurance floor + breach SLA).

**Fallback ladder** (best acceptable first)

1. 24-month general cap + 5x-fees data-breach super-cap + uncapped IP indemnity
2. 18-month general cap + 3x-fees data-breach super-cap + uncapped IP indemnity
3. 12-month general cap (floor) + 2x-fees data-breach super-cap + uncapped IP indemnity

**Walk-away floor**

Direct damages excluded, OR the IP-infringement indemnity capped, OR no super-cap tier for data-breach on a deal processing sensitive data.

**Escalation triggers**

- No super-cap tier for data-breach / security (a single flat cap for all claims)
- Data-breach and confidentiality liability left inside the general 12-month cap
- Exclusion of DIRECT damages (only indirect / consequential should be waived)
- Vendor general cap below 12 months fees
- Willful-misconduct / gross-negligence uncap drafted as a pleading (not finding-of-fact) standard
- Cap measured against the lesser of fees paid or fees due
- Customer cap symmetric to vendor without a security/privacy uplift
- 'Sole and exclusive remedy' language reaching beyond third-party IP-infringement claims

**Rationale**

Liability allocation is the single largest financial exposure in a SaaS buy. A flat 12-month cap that swallows data-breach and IP risk is the most common way vendors shift catastrophic loss onto the customer; the three-tier structure is the defensible ask.


### Indemnification

**Preferred position**

Vendor indemnifies customer for: (a) third-party IP infringement claims against the service, (b) data breach caused by vendor's negligence, (c) violations of law by vendor. Vendor controls defense with customer consent on settlements affecting customer. UNCAPPED for IP and data.

**Acceptable range**

Indemnity scope limited to direct claims (not third-party indirect), with cap proportional to risk. Customer indemnity should be reciprocal only for customer-supplied data.

**Fallback ladder** (best acceptable first)

1. Uncapped IP indemnity + data-breach indemnity at the super-cap
2. Uncapped IP indemnity + data-breach indemnity at the general cap
3. IP indemnity at the enhanced super-cap (last resort if truly uncapped is refused)

**Walk-away floor**

No vendor IP-infringement indemnity, or indemnity capped at 12 months' fees.

**Escalation triggers**

- Vendor IP indemnity capped at 12 months fees or less
- Vendor reserves right to modify the service to avoid infringement without preserving functionality
- Customer indemnity for use of the service (broad)
- No data-breach indemnity

**Rationale**

IP indemnity is what lets the customer keep using the product if a third party asserts infringement; without it the customer bears litigation and re-platforming cost for the vendor's IP choices.


### Termination

**Preferred position**

Customer may terminate for material breach with 30-day cure. Customer may terminate for convenience on 60 days' notice with refund of pre-paid unused fees. Vendor termination for breach only after 30-day cure. Auto-renewal requires 60+ days' opt-out notice with electronic confirmation.

**Acceptable range**

Cure period 15-45 days. Auto-renewal opt-out window 30-90 days. Termination for convenience may be replaced with a cap on early-termination fees if vendor has made specific investment in the engagement.

**Fallback ladder** (best acceptable first)

1. Convenience termination + refund of pre-paid unused fees + 60-day auto-renewal opt-out
2. Termination for breach + capped early-termination fee + 60-day opt-out
3. Termination for breach only + 90-day auto-renewal opt-out

**Escalation triggers**

- No customer termination right beyond breach
- Auto-renewal with under 30 days' opt-out window
- No refund of pre-paid unused fees on convenience termination
- Vendor termination for convenience without refund
- Cure period under 15 days for either party


### Confidentiality

**Preferred position**

Mutual confidentiality for 5 years post-termination, perpetual for trade secrets. Standard exclusions (public knowledge, independently developed, received from third party without restriction). Return or destruction on request with certification.

**Acceptable range**

Confidentiality 3-7 years. One-way confidentiality acceptable where only one party shares.

**Escalation triggers**

- Confidentiality less than 2 years
- No carve-out for compelled disclosure
- No return / destruction obligation
- Confidentiality applies to publicly available information


### Non compete

**Preferred position**

There is NO federal ban on post-employment non-competes. The FTC's 2024 Non-Compete Rule was vacated nationwide before it took effect (Ryan, LLC v. FTC, N.D. Tex. 2024) and the FTC abandoned its appeals in September 2025, so the rule is dead; the FTC now pursues only case-by-case enforcement. Enforceability is governed entirely by state law and varies widely. Limit any non-compete to senior employees with material access to confidential information, tie it to a specific scope / territory and to real consideration, keep it to 12 months or less, and confirm the governing state's law before relying on it.

**Acceptable range**

6-12 months for senior executives where state law permits. VOID in total-ban states (California (Cal. Bus. & Prof. Code 16600), Minnesota, Montana, North Dakota, Oklahoma, Wyoming) and unenforceable above wage thresholds or for certain roles in many others (e.g. Colorado, Illinois, Massachusetts, Maine, Maryland, Nevada, New Hampshire, Oregon, Rhode Island, Virginia, Washington, Washington DC). Where a non-compete is unenforceable, rely on NDAs plus a narrowly drawn non-solicitation. Note a counter-trend: some states (e.g. Florida's CHOICE Act, 2025) make non-competes easier to enforce for high earners.

**Escalation triggers**

- Stating or assuming a federal FTC non-compete ban (there is none; the 2024 rule was vacated)
- Indefinite or > 12 month duration
- Worldwide scope with no business-justification tie
- Post-employment non-compete on employees in a total-ban state (CA, MN, MT, ND, OK, WY)
- Non-compete on rank-and-file (non-senior) employees
- No additional consideration beyond continued employment


### Non solicitation

**Preferred position**

12-month non-solicitation of employees and customers post-termination. Carve-outs for general public job postings and unsolicited applications.

**Acceptable range**

6-24 months. Mutual or unilateral depending on power balance.

**Escalation triggers**

- More than 24 months
- No carve-out for general advertisements / general hires
- Applies to suppliers / vendors as well as customers and employees


### Intellectual property

**Preferred position**

Customer retains all customer data and customer-provided materials. Vendor retains the service and its underlying tools. Customer feedback may be used by vendor only on a non-personal, aggregated basis. No assignment of customer trademark or content beyond what's needed to deliver the service.

**Acceptable range**

Vendor may use de-identified usage data for product improvement. Aggregated benchmarks acceptable if customer cannot be re-identified.

**Escalation triggers**

- Vendor claims any rights in customer data beyond service delivery
- Customer feedback assigned to vendor with personal attribution
- Vendor right to public reference / case study without consent


### Force majeure

**Preferred position**

Standard force majeure (acts of God, war, government action, pandemic). Suspends performance, does not excuse payment obligations. Notice within reasonable time. Right to terminate after 30+ days of continued event.

**Acceptable range**

Termination right after 30-90 days of continued event. Carve-outs for known risks at signing.

**Escalation triggers**

- Force majeure excuses payment obligations
- No termination right on prolonged event
- Includes 'changes in applicable law' as force majeure (too broad)
- No notice obligation


### Dispute resolution

**Preferred position**

Negotiation -> mediation -> binding arbitration before AAA / JAMS, with carve-out for injunctive relief in state or federal court. Seat in home US state. English language. Single arbitrator unless the amount in controversy is at least $3M, in which case three arbitrators by default under AAA Commercial Rule L-2 (effective 2022) absent the parties' contrary agreement. Class-action waiver under the FAA (subject to state-law limits).

**Acceptable range**

State or federal court litigation in mutual jurisdiction. AAA Commercial / JAMS Streamlined Rules acceptable.

**Escalation triggers**

- Drafter-favorable arbitration rules / forum
- Class action waiver without consideration where state law (e.g. CA) limits enforcement
- No carve-out for injunctive relief
- Loser-pays-fees clauses in employment context (FLSA / Title VII concerns)


### Governing law

**Preferred position**

Governing law of organization's home US state (commonly Delaware, New York, or California). Federal court jurisdiction where diversity exists; state court otherwise. Mediation before litigation optional.

**Acceptable range**

Major commercial states (Delaware, New York, California, Texas) acceptable. Arbitration under AAA Commercial Arbitration Rules.

**Escalation triggers**

- Unfavorable or unusual state with no business connection
- Mandatory arbitration in a jurisdiction with class-action-waiver enforcement issues
- Jury waiver in a state where it requires conspicuous notice (e.g. Georgia) without that notice


### Assignment

**Preferred position**

No assignment by either party without prior written consent, not unreasonably withheld. Customer carve-out for affiliate or change-of-control assignment without consent. Vendor change-of-control to a competitor triggers customer termination right.

**Acceptable range**

Free assignment for either party with notice. Restriction acceptable if change-of-control termination right is reciprocal.

**Escalation triggers**

- Vendor free assignment without notice
- Vendor change-of-control without customer termination right
- Customer assignment blocked even for affiliates


### Amendment

**Preferred position**

Amendments require written agreement signed by both parties. No oral modifications.

**Acceptable range**

Email confirmation between authorised representatives may suffice for routine amendments.

**Escalation triggers**

- Unilateral amendment right by one party
- Amendment by website / posting without notice
- Click-through amendments for material terms


### Severability

**Preferred position**

If any provision is held invalid, the remainder remains in effect. Invalid provision is replaced by an enforceable provision approximating the original intent.

**Acceptable range**

Standard severability is non-negotiable; minor wording variation acceptable.

**Escalation triggers**

- Severability that voids the entire agreement
- No reformation right


### Waiver

**Preferred position**

No waiver of any provision is effective unless in writing signed by the waiving party. A single waiver does not constitute a waiver of subsequent breaches.

**Acceptable range**

Standard waiver clause is non-negotiable; minor wording variation acceptable.

**Escalation triggers**

- Implied waiver from course of dealing
- Waiver by a junior employee binding the organisation


### Notices

**Preferred position**

Notices in writing to designated contact, sent by certified US Mail (return receipt) or nationally recognized overnight courier with signature confirmation, or via email with read-receipt. Effective on the earlier of confirmed receipt or 3 business days after dispatch.

**Acceptable range**

Email-only notice acceptable for routine matters; physical notice required for breach / termination.

**Escalation triggers**

- Notice via website / posting only
- Effective date based on dispatch with no rebuttable presumption
- Notice to a generic role rather than a designated person


### Entire agreement

**Preferred position**

This agreement, together with referenced exhibits and SOWs, constitutes the entire agreement and supersedes all prior or contemporaneous understandings, written or oral.

**Acceptable range**

Carve-out for previously executed NDA or other surviving instruments.

**Escalation triggers**

- Carve-out that incorporates oral representations
- Survival of pre-contractual representations not reduced to writing


### Survival

**Preferred position**

Confidentiality, IP ownership, indemnification, limitation of liability, payment for services rendered, and dispute resolution survive termination.

**Acceptable range**

Standard survival list is non-negotiable; minor variation acceptable.

**Escalation triggers**

- All obligations survive (effectively perpetual)
- No survival of confidentiality or IP


### Representations warranties

**Preferred position**

Mutual reps on corporate authority and no-conflict. Provider reps: (a) services performed in a workmanlike manner conforming to specs; (b) deliverables do not infringe or misappropriate any third party's patent, copyright, trademark, or trade secret; (c) authorship -- work is original or properly licensed / assigned; (d) open-source disclosure -- all OSS is listed with its license and no copyleft (GPL / LGPL / AGPL / etc.) component subjects the deliverable to source-disclosure or free-relicensing obligations; (e) no disabling code / malware. Non-infringement and authorship reps are UNQUALIFIED (no knowledge qualifier). AS-IS for everything else. Survival 12-24 months (longer / uncapped for title and non-infringement in an assignment).

**Acceptable range**

Knowledge qualifiers acceptable on forward-looking or third-party-dependent reps, but NOT on authorship or title. Survival 12 months (SaaS) to 36 months (assignments / high value).

**Escalation triggers**

- No non-infringement warranty
- No open-source / copyleft disclosure warranty
- Knowledge qualifier on authorship or title (should be unqualified)
- Survival under 12 months
- Broad fitness-for-purpose warranty with no scope


### Payment terms

**Preferred position**

Net 45 days from receipt of invoice. Right of set-off for amounts due to customer. Disputed amounts withheld pending resolution; undisputed paid timely. Late fee limited to 1% per month or applicable legal cap, whichever is lower.

**Acceptable range**

Net 15-60 days. 0.5%-1.5% late charge.

**Escalation triggers**

- Net under 30 days
- Pre-payment of more than 25% with no milestones
- Late fee in excess of 1.5% per month
- No set-off right or right limited to disputes


### Insurance

**Preferred position**

Vendor maintains, with A-/VII+ rated insurers: Technology E&O of $2M-$5M per claim (a SEPARATE line, not bundled into cyber -- Tech E&O often excludes first-party breach costs); Cyber / network-security & privacy liability of $2M-$5M per claim (required for ANY handling of customer data, not only PII); Commercial General Liability of $1M per occurrence / $2M aggregate; Umbrella / excess of $5M following form; statutory Workers' Comp + $1M employer's liability. Customer named additional insured on CGL, auto, and umbrella (primary and non-contributory). Additional-insured status is NOT available on Tech E&O or cyber (own-services policies) -- require an ACORD certificate, 30 days' notice of cancellation, and coverage at least equal to the liability super-cap.

**Acceptable range**

Limits scale to deal value and data sensitivity: $1M lines for SMB deals; $5M-$10M cyber / Tech E&O for data-heavy or regulated workloads. A combined tech package (E&O + cyber) is acceptable only if the cyber sublimit is separately stated.

**Escalation triggers**

- No cyber coverage where the vendor handles any customer data
- Tech E&O and cyber collapsed into one limit with no cyber sublimit
- Insurance limits below the liability super-cap (coverage gap vs. exposure)
- No additional-insured status on CGL / umbrella
- Additional-insured demanded on Tech E&O or cyber (not available -- use a certificate)
- Self-insurance with no minimum net-worth / financial threshold


### Data protection

**Preferred position**

DPA mandatory. 24-72 hour breach notification with incident details. Sub-processors require advance notice (30 days) with right to object. SOC 2 Type II + ISO 27001 or equivalent annually. Customer owns customer data; vendor's rights limited to providing the service. Data residency controls. Export and deletion within 30 days of termination.

**Acceptable range**

Breach notice 48-72 hours. Sub-processor objection 30-90 days. SOC 2 OR ISO 27001 (not both required). Data residency only where customer has regulatory need.

**Fallback ladder** (best acceptable first)

1. DPA + 24h breach notice + 30-day sub-processor objection + SOC 2 Type II and ISO 27001
2. DPA + 48h breach notice + 30-day sub-processor objection + SOC 2 Type II or ISO 27001
3. DPA + 72h breach notice + notice-only sub-processors + annual SOC 2

**Walk-away floor**

No DPA where personal data is processed, or breach notice longer than 72 hours.

**Escalation triggers**

- No DPA when personal data is processed
- Breach notification window over 72 hours
- Blanket sub-processor authorization without notification
- No data-export tool or post-termination retention exceeding 60 days
- Vendor right to use customer data for product improvement without separate consent

**Rationale**

A weak DPA converts every downstream breach into the customer's regulatory and reputational problem. Breach-notice timing and sub-processor control are the levers that actually matter.


### Audit rights

**Preferred position**

Customer audit right once per year on 30 days' notice. Annual SOC 2 / ISO 27001 report satisfies in lieu of on-site for routine audit. For-cause audits permitted on 10 days' notice. Penetration test summary available on request.

**Acceptable range**

Audit frequency tied to risk; for-cause audits permitted on shorter notice.

**Escalation triggers**

- No audit rights at all
- Audits gated on vendor's auditor selection
- Penetration test results withheld absent confidentiality


### Subcontracting

**Preferred position**

Subcontracting allowed with prior written notice and Customer right to object on reasonable grounds. Vendor remains primarily liable for subcontractor performance and breaches.

**Acceptable range**

Pre-approved subcontractor list with periodic update notice. Less restrictive for routine functions (e.g. data centres).

**Escalation triggers**

- Free subcontracting without notice
- Vendor's liability for subcontractor capped at the subcontractor's own liability
- No reasonable-objection right


### Definitions

**Preferred position**

Definitions section places defined terms alphabetically. Capitalised terms used consistently throughout the agreement.

**Acceptable range**

Standard definitions are non-negotiable; specific definitions are deal-specific.

**Escalation triggers**

- Defined terms used inconsistently in the agreement body
- Material defined terms left undefined or circular


### Preamble

**Preferred position**

Identifies parties (legal name, jurisdiction of formation, registered address), effective date, and references the principal arrangement.

**Acceptable range**

Standard preamble is non-negotiable.

**Escalation triggers**

- Party not legally identifiable from the preamble
- Effective date contingent on a future event without backstop


### Recitals

**Preferred position**

Recitals state the background and purpose. Recitals are not operative and do not create obligations unless explicitly incorporated.

**Acceptable range**

Recitals length proportionate to deal complexity.

**Escalation triggers**

- Recitals contain operative obligations
- Recitals contradict the operative provisions


### Signature block

**Preferred position**

Authorised signatories on each side, named and titled. Date of execution. Counterparts and electronic signature acceptable per the federal E-SIGN Act and applicable state UETA. Avoid wet-ink-only requirements unless real estate / wills / specific state filings require it.

**Acceptable range**

Wet-ink only where required by state filing rules (e.g. some real-estate recordings).

**Escalation triggers**

- Counterparty signatory without authority of record
- Mismatch between named party and signatory entity
- Wet-ink required where E-SIGN / UETA permits electronic signature


### Sla

**Preferred position**

Uptime commitment (commonly 99.9% monthly) measured over a rolling calendar month with a NARROW, defined exclusions list (pre-notified maintenance and genuine force majeure). Tiered service credits that scale meaningfully with downtime. Severity-tiered support with defined response and restoration targets. Chronic-failure termination right with a pro-rata refund of prepaid fees.

**Acceptable range**

99.5%-99.99% depending on tier and price. Credits claimed within 30-60 days. Maintenance excluded only if pre-notified and duration-capped.

**Escalation triggers**

- Uptime below 99.9% or no measured commitment at all
- Broad / undefined exclusions (e.g. 'any factor outside the vendor's control')
- Service credits trivial or capped so low they are not a real remedy
- Credits stated as the sole remedy even for security / data incidents
- No support response or restoration targets


### Residuals

**Preferred position**

No residuals clause by default: unaided general memory is not a licence to use the disclosing party's confidential information. If a residuals clause is accepted, limit it to information retained in the unaided memory of individuals with authorized access, exclude deliberately memorized material, and carve out patents, copyrights, and trade secrets.

**Acceptable range**

Narrow residuals limited to unaided memory, with an express carve-out for IP rights and no licence to trade secrets.

**Escalation triggers**

- Broad residuals clause granting a licence to use confidential information
- Residuals covering deliberately memorized material
- No carve-out for patents, copyrights, or trade secrets


### Order of precedence

**Preferred position**

Explicit order of precedence resolving conflicts between the agreement and its exhibits, order forms, SOWs, and incorporated policies. Negotiated order forms / SOWs control over the base form for their specific subject matter; the master agreement controls on general terms. Incorporated URLs / click-through policies rank lowest and cannot override negotiated terms.

**Acceptable range**

Order form / SOW controls for its subject matter; MSA controls generally. Vendor policy documents rank below negotiated terms.

**Escalation triggers**

- Vendor's unilateral online terms / policies control over the negotiated agreement
- No order-of-precedence clause where multiple documents are incorporated
- Exhibits silently override negotiated protections


### Ai training data

**Preferred position**

The vendor may NOT use customer data, inputs, or outputs to train, fine-tune, or improve any shared AI / ML model except in aggregated, de-identified form that cannot be attributed to the customer, and only where contractually permitted. No use of customer confidential information or personal data for model training absent explicit opt-in.

**Acceptable range**

Aggregated, de-identified improvement of the customer's own tenant only, with an opt-out. No cross-customer model training on identifiable data.

**Escalation triggers**

- Vendor trains foundation / shared models on customer data by default
- No opt-out from model training
- Customer confidential information or personal data used for training
- Training rights survive termination with no deletion obligation


### Ai output ownership

**Preferred position**

As between the parties, the customer owns the outputs generated from its inputs, and the vendor assigns or licenses all rights in those outputs to the customer for its use. The vendor makes no ownership claim over customer-directed outputs. Allocate responsibility for third-party IP in outputs and address the limited copyrightability of purely AI-generated content.

**Acceptable range**

Customer owns or holds a broad, perpetual, royalty-free licence to outputs. Vendor retains rights only in its pre-existing models and technology.

**Escalation triggers**

- Vendor claims ownership of customer-directed outputs
- No allocation of third-party IP infringement risk in outputs
- Customer granted only a narrow or revocable licence to its own outputs


### Custom

**Preferred position**

Use the user-specified instruction. AI inference applies the user's tone and emphasis.

**Acceptable range**

Wide; user-driven.


---

Generated from Vaquill's code-defined playbook templates.
Source: https://vaquill.ai
