# Vaquill Open Legal Resources

> Open, attorney-grade resources for US commercial practice: negotiation playbooks, ready-to-use prompts, reference datasets, and developer tools. Free to use with attribution.

These are Vaquill's own authored resources, the same ones that power [Vaquill](https://vaquill.ai). Nothing here is customer data.

> **Disclaimer.** General US-commercial reference, not legal advice. Verify anything jurisdiction-specific with counsel. See [DISCLAIMER.md](DISCLAIMER.md).

## Prompts

Ready-to-use prompts for working with a legal AI assistant, the same starter prompts that ship inside Vaquill. See [prompts/](prompts/).

- [Composer prompts](prompts/composer-prompts.md) - fully written, ready-to-run prompts by task (triage, review, drafting, negotiation, research, compliance, corporate, disputes).
- [Research templates](prompts/research-templates.md) - fill-in-the-blank templates with placeholders for research and analysis questions.

## Contract due-diligence questions

A vetted question bank for contract review and due diligence: 8 deal types, 145 questions, each tagged with an answer type.
See [contract-diligence-questions/](contract-diligence-questions/).

## US legal doctrines

79 US legal doctrines mapped to their foundational cases, with citations and holding summaries, grouped by substantive area.
See [doctrines/](doctrines/).

## US landlord-tenant rules

A cited 50-state (plus DC) reference database of residential landlord-tenant rules: deposit caps and return windows, notice-to-quit periods, entry notice, late fees, retaliation, and more.
See [landlord-tenant/](landlord-tenant/). General reference only; verify against the current statute.

## US contract clause library

46 balanced, professionally drafted exemplar clauses across 24 clause types, with applicable authorities and tags.
See [clause-library/](clause-library/).

## US legal toolkit (for developers)

Small, dependency-free utilities and datasets: US citation regexes, a CourtListener query normalizer, a state-to-court-ID dataset, and US legal taxonomies.
See [us-legal-toolkit/](us-legal-toolkit/).

## Playbooks

### Commercial

- [AI / Gen-AI Addendum - Customer side](commercial/ai_addendum_customer.md) (Customer side) - You're buying AI / gen-AI features on top of a SaaS or services deal. Secures output ownership, a strict no-training default, an output-infringement indemnit...
- [AI / Gen-AI Addendum - Vendor side](commercial/ai_addendum_vendor.md) (Vendor side) - You're providing AI / gen-AI features. Assigns Output to the customer while retaining your models, defaults to no-training on identifiable data (with de-iden...
- [Consulting / Professional Services - Client side](commercial/consulting_client.md) (Customer side) - You're hiring a consultant or professional services firm. Strong work-product IP transfer, milestone-tied payments, service warranties with named-personnel c...
- [Consulting / Professional Services - Provider side](commercial/consulting_provider.md) (Vendor side) - You're the consultant or professional-services firm being engaged. Retains pre-existing tools and methodologies, assigns deliverables only on full payment, c...
- [License Agreement - Licensee side](commercial/license_licensee.md) (Licensee side) - You're licensing software, data, or IP from a vendor. Locks down scope of use, audit limitations, IP indemnification, and fair use after termination.
- [License Agreement - Licensor side](commercial/license_licensor.md) (Licensor side) - You're licensing your software, data, or IP to a customer. Keeps the grant narrow, reserves all rights not expressly granted, preserves audit / true-up right...
- [M&A Acquisition - Buyer side](commercial/ma_buyer.md) (Customer side) - You're acquiring a private company (stock, asset, or merger). Comprehensive reps with real survival, a robust indemnity backed by escrow / holdback, pro-sand...
- [M&A Acquisition - Seller side](commercial/ma_seller.md) (Vendor side) - You're selling a private company (or its assets). Qualifies reps and shortens survival, caps indemnity to the escrow / R&W retention, makes indemnification t...
- [MSA - Customer side](commercial/msa_customer.md) (Customer side) - Master Services Agreement framework you sign once with a vendor and order against via SOWs. Customer-side: tighter warranties, IP-favorable on deliverables,...
- [MSA - Vendor side](commercial/msa_vendor.md) (Vendor side) - Vendor-side MSA template. Tight liability cap, IP retained, payment discipline, and reasonable termination protections.
- [Professional Services (PSA + SOW) - Client side](commercial/psa_client.md) (Customer side) - Master services agreement you sign once and order against via SOWs. Client-side: own deliverables as created, a real acceptance / rejection right, and an SOW...
- [Professional Services (PSA + SOW) - Provider side](commercial/psa_provider.md) (Vendor side) - Provider-side master services agreement. Assigns deliverables on payment, keeps a deemed-acceptance mechanic, retains tools and methodologies, and caps liabi...
- [Reseller / Channel - Reseller side](commercial/reseller_reseller.md) (Other side) - You're the reseller, distributor, or channel partner. Secures workable margins and price protection, a real supplier IP / product indemnity, deal-registratio...
- [Reseller / Channel - Supplier side](commercial/reseller_supplier.md) (Vendor side) - You're the vendor appointing a reseller or channel partner. Keeps the brand license narrow and revocable, sets pricing floors, flows your EULA through to end...
- [SaaS - Customer side](commercial/saas_customer.md) (Customer side) - You're buying SaaS from a vendor. Tightens liability cap protections, secures IP and data-breach indemnities, locks down auto-renewal and data-portability ri...
- [SaaS - Vendor side](commercial/saas_vendor.md) (Vendor side) - You're selling SaaS. Caps liability proportionally, scopes indemnification to IP infringement, secures payment discipline, and protects feedback / usage data...
- [Service Level Agreement (SLA) - Customer side](commercial/sla_customer.md) (Customer side) - You're the customer negotiating uptime and support commitments. Pushes a meaningful uptime target, narrow exclusions, real service credits, and a right to wa...
- [Service Level Agreement (SLA) - Vendor side](commercial/sla_vendor.md) (Vendor side) - You're the vendor committing to uptime. Keeps the target achievable, the exclusions realistic, credits as the sole financial remedy, and downtime liability b...

### Privacy & Data

- [DPA - Controller side](privacy/dpa_controller.md) (Customer side) - You're the data controller pushing personal data to a vendor (processor). Locks down breach SLAs, sub-processor approval, audit, deletion, and cross-border t...
- [DPA - Processor side](privacy/dpa_processor.md) (Vendor side) - You're the SaaS / service vendor processing customer data. Anchors realistic breach SLAs, sub-processor notice patterns, and limits liability outside vendor...
- [HIPAA BAA - Business Associate side](privacy/baa_business_associate.md) (Vendor side) - You're the vendor / business associate handling PHI. Commits to the mandatory BAA obligations while keeping breach windows operationally workable, capping li...
- [HIPAA BAA - Covered Entity side](privacy/baa_covered_entity.md) (Customer side) - You're the covered entity (or upstream business associate) sharing PHI with a vendor. Locks the BA to permitted uses, tight breach notice, subcontractor flow...

### Non-Disclosure

- [Mutual NDA](nda/nda_mutual.md) (Other side) - Two-way confidentiality for evaluation discussions, due diligence, or pre-contract collaboration. Balanced obligations on both sides; sensible carve-outs for...
- [One-way NDA - Receiving party](nda/nda_unilateral_receiving.md) (Other side) - You're being asked to sign an NDA receiving the other side's confidential information (e.g. you're a consultant under a client's NDA, or you're evaluating a...

### HR & Employment

- [Employment - Employee side](hr/employment_employee.md) (Other side) - You're the employee or candidate reviewing an offer or employment agreement. Narrows IP assignment to work within scope, rejects non-competes where they are...
- [Employment - Employer side](hr/employment_employer.md) (Employer side) - Standard offer-letter / employment-contract positions for the employer. Reasonable confidentiality + IP assignment, jurisdiction-aware non-compete handling,...

### Intellectual Property

- [IP Assignment - Assignee side](ip/ip_assignment_assignee.md) (Other side) - You're receiving IP from a contractor, founder, or acquired company. Locks down full assignment of work product, trailing IP delivery, moral-rights waiver wh...
- [IP Assignment - Assignor side](ip/ip_assignment_assignor.md) (Other side) - You're the party assigning IP (a contractor, founder, or seller). Assigns only the specifically identified work, retains background IP with a license-back, w...

---

28 playbooks. Regenerate with `python -m scripts.export_playbooks_md` (Vaquill monorepo).

## License

Licensed under [CC BY 4.0](LICENSE). Use freely, including commercially, with attribution to Vaquill.
