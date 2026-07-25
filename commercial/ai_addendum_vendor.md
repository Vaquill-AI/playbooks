# AI / Gen-AI Addendum - Vendor side

> You're providing AI / gen-AI features. Assigns Output to the customer while retaining your models, defaults to no-training on identifiable data (with de-identified operational use), and keeps the output indemnity and accuracy disclaimers workable.

**Side:** Vendor · **Jurisdiction:** US

**Best fit for:**

- Vendor shipping AI / gen-AI features on a SaaS product
- Adding an AI addendum to your standard SaaS terms

**Tags:** `ai`, `genai`, `llm`, `addendum`, `vendor`

_General US-commercial reference, not legal advice. Verify anything jurisdiction-specific with counsel._

33 clauses.

---

### Limitation of liability

**Preferred position**

AI Output may be inaccurate or incomplete; human review is required for material decisions; no warranty of accuracy or fitness for a particular decision (distinct from the service-availability warranty). Standard super-cap / uncapped carve-outs (data breach, IP indemnity, fraud, willful misconduct) otherwise apply.

**Acceptable range**

General cap 1x-2x (or 12-24 months) fees. Super-cap 2x-5x for data/security and confidentiality. IP indemnity uncapped or super-capped. Mutual where possible; aggregate, not per-claim.

**Escalation triggers**

- Accuracy or 'no hallucination' warranty on Outputs
- Uncapped liability for Output errors
- Liability for the customer's reliance on Outputs without human review

**Rationale**

AI Outputs are probabilistic, so an accuracy or no-hallucination warranty, or uncapped liability for Output errors, would make the vendor an insurer of results no model can guarantee.


### Indemnification

**Preferred position**

Vendor's output indemnity is limited to Outputs of the vendor's own models used UNMODIFIED, excluding customer prompts, customer data, customer modifications, and combinations with non-vendor tools; capped consistent with the master terms. Third-party model-provider issues outside the vendor's control are handled via the model provider, not an uncapped vendor guarantee.

**Acceptable range**

IP indemnity uncapped or super-capped; data-breach indemnity capped at the liability super-cap. Knowledge / prejudice qualifiers on the procedural conditions are fine; the indemnity scope itself should not be knowledge-qualified.

**Fallback ladder** (best acceptable first)

1. Output indemnity limited to unmodified-model Outputs, excluding customer prompts, data, and modifications, and capped in line with the master terms.
2. Output indemnity applies at a higher negotiated cap, still excluding customer-prompt-caused and third-party model-provider infringement.
3. Output indemnity applies only where the customer uses the current model version and vendor content filters, capped at the master-terms limit.

**Walk-away floor**

Uncapped output indemnity, or an indemnity covering customer-prompt-caused, modified-Output, or third-party model-provider infringement.

**Escalation triggers**

- Uncapped output indemnity
- Indemnity covering customer-prompt-caused or modified-Output infringement
- Indemnity for third-party model-provider conduct beyond the vendor's control

**Rationale**

An uncapped output indemnity, or one that reaches customer-prompt-caused infringement or third-party model-provider conduct, exposes the vendor to open-ended liability for risks outside its control.


### Termination

**Preferred position**

Mutual termination for material breach with 30-day cure (10 days for payment breaches; general-breach cure ranges 30-90 days). Termination for convenience is a customer-favorable ask, not an automatic default: where granted, make it Customer-only on 30-90 days' notice, paying through the termination date. Insolvency / change-of-control trigger immediate termination.

**Acceptable range**

Cure period 15-60 days. Termination for convenience may be Customer-only or absent if discounted pricing warrants it.

**Escalation triggers**

- Cure period less than 10 days for either party
- Vendor-only termination for convenience without refund
- No termination right on insolvency
- Penalty / acceleration on termination for convenience


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

Each party retains its pre-existing IP. For custom deliverables, the customer owns them via a present ('hereby assigns') assignment -- do NOT rely on 'work made for hire' alone, because under 17 U.S.C. 101 only nine enumerated categories qualify and software / most custom code is not among them. Moral rights (VARA, 17 U.S.C. 106A) are WAIVED and not-asserted, never 'assigned.' Vendor retains the service, tools, and methodologies. Feedback: the US market default is a broad, perpetual, royalty-free, irrevocable license to the vendor, used AS IS, with no public attribution of the customer as source without consent. Any open-source components are disclosed with their licenses.

**Acceptable range**

Vendor ownership of the service with a broad customer license is standard for SaaS; present-assignment of custom deliverables to the customer. A feedback license narrowed to de-identified / aggregated use is the customer-side win.

**Escalation triggers**

- 'Work made for hire' with no present-assignment backstop for non-Section-101 works (fails for software)
- Moral rights purportedly 'assigned' rather than waived (incoherent under US law)
- Broad IP assignment sweeping in pre-existing / background IP
- Feedback license granting public attribution of the customer without consent
- No open-source disclosure where deliverables include third-party code


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

No assignment without prior written consent, not to be unreasonably withheld. Carve-out for assignment to affiliate or in connection with merger / acquisition / change of control.

**Acceptable range**

Free assignment for either party with notice. Restriction acceptable if change-of-control termination right is reciprocal.

**Escalation triggers**

- Unilateral assignment right without consent
- Anti-assignment with no merger / affiliate carve-out
- Assignment voids the agreement automatically


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

Net 30 days from the date of a correct invoice (the standard market trigger; 'from receipt' is a payor-favorable variant that must be stated expressly). Disputed amounts identified within 10 business days. Late charge 1.5% per month or maximum permitted by state usury law on undisputed overdue amounts. Currency: USD. Sales / use tax excluded except where required by law.

**Acceptable range**

Net 15-60 days. 0.5%-1.5% late charge.

**Escalation triggers**

- Pre-payment of more than 30% with no milestones
- Net > 90 days
- Late fee in excess of state usury cap
- Right of set-off broader than disputed amounts


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

DPA required when personal data is processed. Contractual processor / service-provider obligations under the comprehensive US state consumer-privacy laws now in effect (20 states as of 2026, including CA (CCPA/CPRA), VA, CO, CT, UT, TX, OR, MT, and others). Identify and comply with the law(s) of the state(s) where the data subjects reside. 72-hour breach notification (some states mandate sooner -- e.g. Florida 30 days for state agencies). Standard contractual clauses or alternative transfer mechanism for cross-border transfers (especially to/from EEA). Annual SOC 2 / ISO 27001 right.

**Acceptable range**

DPA with reasonable negotiation of sub-processor notice period. Breach notification within 48-72 hours; HIPAA business associates: 60 days max.

**Escalation triggers**

- No DPA when personal data is processed
- Blanket sub-processor authorization without notification
- Breach notification exceeding 72 hours (or applicable state floor)
- No CCPA service-provider language where customer is a California business
- No HIPAA BAA where PHI is processed


### Audit rights

**Preferred position**

Once per year on 30 days' notice during business hours, with confidentiality protections. SOC 2 Type II / ISO 27001 reports satisfy in lieu of on-site audit. Customer pays its own audit costs absent material non-compliance.

**Acceptable range**

Audit frequency tied to risk; for-cause audits permitted on shorter notice.

**Escalation triggers**

- No audit rights at all
- Vendor-controlled audit selection
- Audit findings not actionable
- Customer must pay vendor's audit costs even where material non-compliance exists


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

Default: no training on customer-identifiable data. Vendor may use de-identified and aggregated data to operate and improve features, provided AS IS and not in a customer-specific model. Model fine-tuning on a customer's data requires that customer's opt-in. Standard operational logs retained for security / abuse-prevention for a limited period.

**Acceptable range**

Aggregated, de-identified improvement of the customer's own tenant only, with an opt-out. No cross-customer model training on identifiable data.

**Fallback ladder** (best acceptable first)

1. No training on customer-identifiable data; vendor keeps de-identified, aggregated use to operate and improve features and retains security logs for a limited period.
2. Vendor limits improvement use to de-identified, aggregated data and shortens the security-log retention window on request.
3. Vendor uses operational data only for security and abuse prevention, drops general improvement use, and deletes logs after a fixed short period.

**Walk-away floor**

Customer bars all de-identified, aggregated operational use, or demands immediate deletion of all security and abuse-prevention logs the service needs to run.

**Escalation triggers**

- Customer demands immediate deletion of all operational / security logs
- No ability to use de-identified, aggregated data to run and improve the service
- Unlimited customer audit of the vendor's training pipeline or model weights

**Rationale**

Operating and improving the service depends on de-identified, aggregated data and short-lived security logs, so a customer demand to delete all logs or bar all improvement use would break the product's operability and abuse defenses.


### Ai output ownership

**Preferred position**

As between the parties the customer owns Outputs; the vendor assigns its rights in Outputs but RETAINS its models, weights, methodologies, and improvements. Vendor may use de-identified, aggregated Inputs / Outputs to operate, secure, and improve the service. Outputs are not warranted to be unique and similar Outputs may be generated for others.

**Acceptable range**

Customer owns or holds a broad, perpetual, royalty-free licence to outputs. Vendor retains rights only in its pre-existing models and technology.

**Fallback ladder** (best acceptable first)

1. Customer owns its Outputs; vendor retains its models, weights, methodologies, and improvements, and keeps de-identified, aggregated operational use.
2. Vendor assigns Outputs and narrows operational use to security and service operation, dropping the 'improve the service' language while keeping model ownership.
3. Vendor grants the customer a perpetual license to its Outputs instead of assignment, still retaining all model IP.

**Walk-away floor**

Customer claims ownership of the vendor's models, weights, or improvements, or demands exclusivity over commodity Outputs.

**Escalation triggers**

- Customer claims ownership of the vendor's models, weights, or improvements
- Vendor barred from de-identified / aggregated operational use
- Customer demands exclusivity over commodity Outputs

**Rationale**

Assigning Outputs is fine, but a customer claim over our models, weights, or de-identified operational use would give away the core IP the whole product is built on.


### Custom

**Preferred position**

Use the user-specified instruction. AI inference applies the user's tone and emphasis.

**Acceptable range**

Wide; user-driven.


---

Generated from Vaquill's code-defined playbook templates.
Source: https://vaquill.ai
