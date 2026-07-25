# Service Level Agreement (SLA) - Vendor side

> You're the vendor committing to uptime. Keeps the target achievable, the exclusions realistic, credits as the sole financial remedy, and downtime liability bounded.

**Side:** Vendor · **Jurisdiction:** US

**Best fit for:**

- Vendor's standard SLA / uptime commitment
- Publishing an SLA attachment with your SaaS terms

**Tags:** `sla`, `uptime`, `service-credits`, `vendor`

_General US-commercial reference, not legal advice. Verify anything jurisdiction-specific with counsel._

33 clauses.

---

### Limitation of liability

**Preferred position**

Service credits are the sole and exclusive financial remedy for availability failures; no consequential or indirect damages for downtime. Availability failures do not by themselves breach the security / data-protection obligations unless they cause an incident covered there.

**Acceptable range**

General cap 1x-2x (or 12-24 months) fees. Super-cap 2x-5x for data/security and confidentiality. IP indemnity uncapped or super-capped. Mutual where possible; aggregate, not per-claim.

**Fallback ladder** (best acceptable first)

1. Credits are the sole and exclusive financial remedy for downtime; no consequential or indirect damages
2. Credits sole for availability, with availability failures carved out of the security / data-protection obligations unless they cause a covered incident
3. Credits sole for downtime, capped at a stated percentage of the affected monthly fee

**Walk-away floor**

Downtime liability extends beyond the agreed service credits, OR consequential / indirect damages become recoverable for outages.

**Escalation triggers**

- Downtime liability beyond the agreed service credits
- Consequential / indirect damages recoverable for outages

**Rationale**

Keeping credits as the sole financial remedy for downtime is the cap on the vendor's SLA exposure; losing it exposes every outage to consequential-damages claims.


### Indemnification

**Preferred position**

Mutual indemnification for third-party IP-infringement and confidentiality breaches; add a data-breach indemnity where personal data is processed. The IP-infringement indemnity is UNCAPPED or under a separate super-cap (2x-5x fees), NOT subject to the general liability cap -- treating it as capped-at-fees is a vendor-favorable ask, not the neutral default. Defense mechanics: prompt written notice, indemnitor controls defense and settlement, indemnitee cooperates -- with notice/cooperation failures excusing the indemnitor only to the extent of ACTUAL PREJUDICE. Indemnitee consent required for any settlement imposing non-monetary obligations, admitting fault, or not fully releasing it. IP remedies: procure the right to continue, modify without materially reducing functionality, replace, or refund unamortized fees.

**Acceptable range**

IP indemnity uncapped or super-capped; data-breach indemnity capped at the liability super-cap. Knowledge / prejudice qualifiers on the procedural conditions are fine; the indemnity scope itself should not be knowledge-qualified.

**Escalation triggers**

- IP-infringement indemnity 'subject to the overall liability cap' rather than uncapped / super-capped
- Notice / cooperation conditions that forfeit the indemnity without requiring actual prejudice
- No indemnitee consent over settlements imposing non-monetary obligations or fault admissions
- Modify-to-cure remedy that does not preserve materially equivalent functionality
- Indemnity silent on whether it sits inside or above the liability cap


### Termination

**Preferred position**

Any chronic-failure termination right is narrowly bounded: it triggers only on a material, sustained miss (e.g. the committed level missed in three consecutive months, excluding isolated events and excluded downtime), requires written notice within a defined window, and gives the vendor a cure period before termination takes effect. Any refund is limited to prepaid, unused fees for the terminated period. No termination for convenience, no damages, and no refund of fees already consumed.

**Acceptable range**

Cure period 15-60 days. Termination for convenience may be Customer-only or absent if discounted pricing warrants it.

**Escalation triggers**

- Termination for a single month's miss or for excluded downtime
- No cure period before a chronic-failure termination takes effect
- Refund extends beyond prepaid, unused fees (e.g. damages or consumed fees)
- Termination for convenience dressed up as an SLA remedy

**Rationale**

A loosely drafted chronic-failure exit lets the customer walk on a single miss or recover consumed fees, so the trigger, cure period, and refund scope all need to be bounded.


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

Uptime commitment (e.g. 99.9%) measured by the vendor's monitoring, with a defined exclusions list: scheduled maintenance with notice, customer-caused issues, force majeure, and third-party / beyond-the-vendor's-control events. Service credits are the SOLE AND EXCLUSIVE remedy for downtime, must be requested within 30 days, and are capped at a stated percentage of the affected monthly fee. Support response targets are commercially reasonable, not guaranteed resolution times.

**Acceptable range**

99.5%-99.99% depending on tier and price. Credits claimed within 30-60 days. Maintenance excluded only if pre-notified and duration-capped.

**Fallback ladder** (best acceptable first)

1. 99.9% measured by vendor monitoring, full exclusion list, credits capped and sole
2. 99.9% with a premium-tier path to 99.95% and scheduled-maintenance / customer-caused exclusions
3. 99.95% only on a premium tier, exclusions kept broad enough to cover third-party and beyond-control events

**Walk-away floor**

Uptime above 99.95% without a premium tier, OR exclusions narrowed to force majeure only, OR guaranteed resolution (not response) times.

**Escalation triggers**

- Uptime commitment above 99.95% without a premium tier
- Exclusions narrowed to force majeure only
- Credits not the sole remedy, or no cap on credits
- Guaranteed resolution (not response) times
- Retroactive penalty damages for downtime beyond credits

**Rationale**

The committed uptime number and its exclusions define the vendor's operational exposure; an over-promised target or force-majeure-only exclusions turn every outage into a breach.


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
