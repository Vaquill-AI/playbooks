# US Legal Toolkit

A small, dependency-free toolkit for working with US legal citations, court identifiers, and contract taxonomies.
Everything here is plain Python (stdlib only) plus a few JSON datasets, so it drops into any project without new dependencies.

## What is inside

### 1. US citation patterns (`citations/us_citation_patterns.py`)

Compiled regular expressions that recognize US legal authorities in free text: federal and state statutes, the Code of Federal Regulations, federal and state reporter citations, and case captions.
The patterns match citation structure rather than enumerating every reporter, so they generalize across the many state citation formats.
The main entry point is `looks_like_us_citation(text)`, which returns `True` when the text contains an unambiguous US citation.

### 2. CourtListener query normalizer (`citations/courtlistener_query.py`)

Pure functions that clean up search queries before sending them to the CourtListener REST API.
They normalize curly Unicode quotes and dashes, expand common citation abbreviations, strip a stray Boolean `AND` inserted between party names, and help decide whether a string looks like a single case reference.

### 3. Court-ID dataset (`data/state-court-ids.json`)

Two maps keyed by 2-letter US state code: one from state to its CourtListener court IDs (supreme and appellate courts), and one from state to the federal circuit whose decisions bind it.
See `data/README` for the field-by-field description.

### 4. Area-to-title and contract taxonomy datasets (`data/area-to-usc-cfr-titles.json`, `data/us-contract-taxonomy.json`)

`area-to-usc-cfr-titles.json` is a crosswalk from a substantive legal area (patent, tax, labor, and so on) to the US Code and Code of Federal Regulations titles most relevant to it.
`us-contract-taxonomy.json` is a set of enumerated label lists for US contract and compliance work: contract types, party sides, clause types, response categories, regulation types, and document categories.

## Quickstart

Recognize a US citation:

```python
from citations.us_citation_patterns import looks_like_us_citation

looks_like_us_citation("See 15 U.S.C. 78j(b).")        # True
looks_like_us_citation("Brown v. Board, 347 U.S. 483") # True
looks_like_us_citation("summarize the meeting notes")  # False
```

Clean a query for the CourtListener REST API:

```python
from citations.courtlistener_query import normalize_query_for_courtlistener

normalize_query_for_courtlistener("VTX Commc'ns, LLC AND AT&T Inc.")
# "VTX Communications, LLC AT&T Inc."
```

Look up the courts that bind a state, or the USC/CFR titles for an area:

```python
import json

courts = json.load(open("data/state-court-ids.json"))
courts["state_to_cl_court_ids"]["ca"]      # ["cal", "calappdeptsuper", ...]
courts["state_to_federal_circuit"]["ca"]   # "ca9"

crosswalk = json.load(open("data/area-to-usc-cfr-titles.json"))
crosswalk["areas"]["patent"]               # {"usc_titles": [35], "cfr_titles": [37]}
```

## Tests

```bash
pytest tests/
# or, with no pytest installed:
python tests/test_us_citation_patterns.py
python tests/test_courtlistener_query.py
```

---

Provided as-is for developers, not legal advice.
See [../DISCLAIMER.md](../DISCLAIMER.md).

Licensed under [CC BY 4.0](../LICENSE).
