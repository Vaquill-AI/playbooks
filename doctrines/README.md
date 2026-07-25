# US Legal Doctrines to Landmark Cases

This is a curated map of US legal doctrines to their foundational authorities.
Each record names a doctrine, places it in a substantive area, describes it in one or two sentences, and links it to the landmark cases and statutes that established it.
The dataset covers 79 doctrines, 196 cases, and 69 statutory references.

Citations follow Bluebook short form and point to the official reporter for each authority.
The dataset was hand curated and is intended as a study and grounding reference, not as a substitute for reading the decisions themselves.

## Counts by substantive area

| Substantive area | Doctrines |
| --- | --- |
| Bankruptcy | 3 |
| Civil Procedure | 12 |
| Civil Rights | 5 |
| Constitutional Law | 13 |
| Copyright | 1 |
| Criminal Law and Procedure | 13 |
| Evidence | 3 |
| General and Commercial | 22 |
| Immigration | 1 |
| Labor and Employment | 2 |
| Patent | 1 |
| Securities | 3 |
| **Total** | **79** |

## Record schema

Each doctrine record has the following fields.

| Field | Type | Description |
| --- | --- | --- |
| doctrine_name | string | The common name of the doctrine. |
| substantive_area | string | The area of law the doctrine belongs to. |
| description | string | A one or two sentence description of the doctrine. |
| canonical_cases | array | The landmark cases that established the doctrine. |
| canonical_statutes | array | The statutes or rules tied to the doctrine. |

Each entry in `canonical_cases` has these fields.

| Field | Type | Description |
| --- | --- | --- |
| case_name | string | The case name. |
| citation | string | The Bluebook citation. |
| year | number | The year of the decision. |
| court | string | The deciding court. |
| holding | string | A short distillation of the holding. |

Each entry in `canonical_statutes` has these fields.

| Field | Type | Description |
| --- | --- | --- |
| citation | string | The Bluebook citation of the rule or statute. |
| title | string | A short title for the provision. |
| text | string | The quoted or summarized statutory text. |
| source_type | string | The kind of source (usc, cfr, ucc, restatement, or other). |
| title_number | string or null | The code title number where one applies. |
| url | string | A public link to the provision. |

## Example entries

### Brady rule (prosecutorial disclosure)

Substantive area: Criminal Law and Procedure.

The Due Process requirement that prosecutors disclose material evidence favorable to the accused.

| Case | Citation | Year | Court | Holding |
| --- | --- | --- | --- | --- |
| Brady v. Maryland | 373 U.S. 83 | 1963 | Supreme Court of the United States | Suppression by the prosecution of evidence favorable to the accused violates due process where the evidence is material to guilt or punishment, irrespective of good or bad faith. |
| Giglio v. United States | 405 U.S. 150 | 1972 | Supreme Court of the United States | Brady disclosure obligations include impeachment evidence affecting the credibility of prosecution witnesses, such as promises of leniency. |
| United States v. Bagley | 473 U.S. 667 | 1985 | Supreme Court of the United States | Materiality means a reasonable probability that, had the evidence been disclosed, the result of the proceeding would have been different. |
| Kyles v. Whitley | 514 U.S. 419 | 1995 | Supreme Court of the United States | The prosecution's Brady duty extends to evidence known only to police investigators; materiality is assessed cumulatively, not item-by-item. |

### Erie doctrine

Substantive area: Civil Procedure.

The rule governing when federal courts sitting in diversity must apply state substantive law versus federal procedural law.

| Case | Citation | Year | Court | Holding |
| --- | --- | --- | --- | --- |
| Erie Railroad Co. v. Tompkins | 304 U.S. 64 | 1938 | Supreme Court of the United States | Federal courts sitting in diversity must apply state substantive law; there is no general federal common law. |
| Hanna v. Plumer | 380 U.S. 460 | 1965 | Supreme Court of the United States | When a Federal Rule of Civil Procedure directly conflicts with state law and is constitutional under the Rules Enabling Act, the federal rule applies. |
| Guaranty Trust Co. v. York | 326 U.S. 99 | 1945 | Supreme Court of the United States | Adopted the outcome-determinative test: if applying federal procedure would significantly affect the outcome of the case, the federal court should follow state law. |

## Suggested uses

Use it as a study aid to connect a doctrine to the cases that created it.
Use it as a grounding reference for a legal AI system so that answers cite real, verifiable authorities.
Use it for citation checking to confirm that a doctrine is being attributed to the correct landmark case.

## Layout

`doctrines.json` holds the full cleaned dataset.
`by-area/` holds one Markdown file per substantive area with readable case tables.

---

General reference, not legal advice. Verify every authority against the official reporter. See [../DISCLAIMER.md](../DISCLAIMER.md).

Licensed under [CC BY 4.0](../LICENSE).
