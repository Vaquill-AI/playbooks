"""Query normalization helpers for the CourtListener REST API.

Machine-generated or condensed search queries often contain reporter-style
abbreviations that a case-name index does not expand, curly Unicode quotes and
dashes that break Lucene tokenization, and a literal Boolean ``AND`` inserted
between party names (which the index treats as a Lucene operator requiring both
tokens to appear). Any of these can turn a query for a case that exists into
zero hits.

This module provides small, pure functions (no I/O, easy to test) to clean such
queries before sending them to the CourtListener REST API:

  - ``normalize_query_for_courtlistener`` normalizes punctuation, expands common
    citation abbreviations, and strips a stray ``AND`` between corporate parties.
  - ``looks_like_case_name`` decides whether a string looks like a single case
    reference (useful for deciding whether to retry with a ``caseName:`` field
    query).
  - ``extract_party_terms`` pulls the distinctive party tokens out of a case
    name for building a ``caseName:(...)`` field search.
"""

from __future__ import annotations

import re

# Common law-citation abbreviations -> full word. Based on Bluebook T.6 plus
# abbreviations observed in real queries. Conservative list: only abbreviations
# that are unambiguous in a case-name context are expanded.
_ABBREVIATION_EXPANSIONS: list[tuple[str, str]] = [
    (r"\bCommc'?ns\b", "Communications"),
    (r"\bMgmt\.?\b", "Management"),
    (r"\bMfg\.?\b", "Manufacturing"),
    (r"\bIndem\.?\b", "Indemnity"),
    (r"\bIns\.?\b", "Insurance"),
    (r"\bAss'?n\b", "Association"),
    (r"\bDep'?t\b", "Department"),
    (r"\bInt'?l\b", "International"),
    (r"\bNat'?l\b", "National"),
    (r"\bBros\.?\b", "Brothers"),
    (r"\bConstr\.?\b", "Construction"),
    (r"\bSvcs?\.?\b", "Services"),
    (r"\bUniv\.?\b", "University"),
    (r"\bHosp\.?\b", "Hospital"),
    (r"\bAuth\.?\b", "Authority"),
    (r"\bComm'?n\b", "Commission"),
]

# Unicode punctuation that breaks Lucene tokenization.
_QUOTE_NORMALIZATIONS: list[tuple[str, str]] = [
    ("‘", "'"),  # left single quote
    ("’", "'"),  # right single quote
    ("“", '"'),  # left double quote
    ("”", '"'),  # right double quote
    ("–", "-"),  # en dash
    ("—", "-"),  # em dash
]

# Corporate suffixes that mark a party boundary in a case name.
# Word-boundary on the left + boundary-or-terminal lookahead on the right
# so `Co` inside `Communications` doesn't match.
_PARTY_SUFFIX_TOKENS = r"LLC|L\.L\.C\.|Inc\.?|Corp\.?|Co\.?|Ltd\.?|LP|L\.P\.|N\.A\.|P\.C\."
_PARTY_SUFFIXES = rf'\b(?:{_PARTY_SUFFIX_TOKENS})(?=\s|,|;|$|\)|")'

# Matches a stray Boolean ``AND`` joining two corp-shaped parties, e.g.
# ``VTX Commc'ns, LLC AND AT&T Inc.``. The pattern requires a trailing
# corporate suffix before the AND so we don't strip genuine boolean queries
# like ``contract AND negligence``.
_STRAY_AND_BETWEEN_PARTIES = re.compile(
    rf",\s*{_PARTY_SUFFIXES}\s+AND\s+",
    flags=re.IGNORECASE,
)

# Detects a case-name shape: explicit `v.`/`vs.` or two corp-shaped
# parties separated by less than ~80 chars.
_VS_PATTERN = re.compile(r"\b(?:v\.|vs\.|vs)\s+\S", flags=re.IGNORECASE)
_TWO_PARTY_PATTERN = re.compile(
    rf"{_PARTY_SUFFIXES}.{{0,80}}{_PARTY_SUFFIXES}",
    flags=re.IGNORECASE,
)


def normalize_query_for_courtlistener(q: str) -> str:
    """Deterministic cleanup for CourtListener search queries.

    1. Normalize curly quotes and dashes to ASCII.
    2. Expand reporter-style abbreviations (``Commc'ns`` -> ``Communications``).
    3. Strip a stray ``AND`` only when it joins two corp-shaped parties.

    Idempotent. Safe to call on any string.
    """
    if not q:
        return q
    out = q
    for src, dst in _QUOTE_NORMALIZATIONS:
        out = out.replace(src, dst)
    for pattern, replacement in _ABBREVIATION_EXPANSIONS:
        out = re.sub(pattern, replacement, out, flags=re.IGNORECASE)
    out = _STRAY_AND_BETWEEN_PARTIES.sub(lambda m: m.group(0).replace(" AND ", " "), out)
    out = re.sub(r"\s{2,}", " ", out).strip()
    return out


# A converted boolean/topical query wraps groups in parens and quotes phrases
# (e.g. `("limited liability company" OR LLC) AND (...)`). Those characters
# never appear in a natural case reference ("Smith v. Jones", "In re: Grand
# Jury"), so their presence is a reliable "machine-built query" signal.
_BOOLEAN_QUERY_MARKERS = re.compile(r"""[()"]""")


def looks_like_case_name(q: str) -> bool:
    """True when ``q`` looks like a single case reference.

    Useful for deciding whether to retry a zero-result search with a
    ``caseName:`` field query rather than a full-text query.
    """
    if not q:
        return False
    # A converted boolean/topical query is machine-built, never a single case
    # reference. Letting it reach a caseName: field query would produce
    # unbalanced-paren queries that the API rejects.
    if _BOOLEAN_QUERY_MARKERS.search(q):
        return False
    if _VS_PATTERN.search(q):
        return True
    if _TWO_PARTY_PATTERN.search(q):
        return True
    return False


def extract_party_terms(q: str) -> list[str]:
    """Pull party-distinctive tokens out of a case-name query.

    Strips corporate suffixes, Boolean operators, ``v.`` separators, and
    punctuation, then returns the remaining tokens (length > 1). Callers
    typically join them into ``caseName:(t1 t2 ...)`` for a field search.
    """
    if not q:
        return []
    cleaned = re.sub(_PARTY_SUFFIXES, " ", q, flags=re.IGNORECASE)
    cleaned = re.sub(r"\b(?:AND|OR|NOT|v\.|vs\.|vs)\b", " ", cleaned, flags=re.IGNORECASE)
    # Strip parens and quotes too: a boolean/phrase query that slips through
    # would otherwise emit tokens like `("limited` or `"C-`, building an
    # unbalanced caseName:(...) the API rejects.
    cleaned = re.sub(r"""[,.;:()"'`]""", " ", cleaned)
    return [t for t in cleaned.split() if len(t) > 1]
