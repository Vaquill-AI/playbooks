"""Standalone unit tests for courtlistener_query.

Run with: pytest, or `python -m pytest tests/`, from the repo root.
Stdlib only, no external dependencies.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from citations.courtlistener_query import (  # noqa: E402
    extract_party_terms,
    looks_like_case_name,
    normalize_query_for_courtlistener,
)


def test_expands_abbreviation():
    out = normalize_query_for_courtlistener("VTX Commc'ns, LLC")
    assert "Communications" in out
    assert "Commc" not in out


def test_strips_stray_and_between_parties():
    out = normalize_query_for_courtlistener("VTX Commc'ns, LLC AND AT&T Inc.")
    assert " AND " not in out
    assert "Communications" in out


def test_keeps_genuine_boolean_query():
    out = normalize_query_for_courtlistener("contract AND negligence")
    assert " AND " in out


def test_normalizes_curly_quotes_and_dashes():
    out = normalize_query_for_courtlistener("“Smith” – Jones")
    assert "“" not in out
    assert "–" not in out


def test_is_idempotent():
    once = normalize_query_for_courtlistener("Nat'l Ass'n of Mfrs.")
    twice = normalize_query_for_courtlistener(once)
    assert once == twice


def test_looks_like_case_name_true_for_vs():
    assert looks_like_case_name("Smith v. Jones")


def test_looks_like_case_name_false_for_boolean_query():
    assert not looks_like_case_name('("limited liability" OR LLC) AND fraud')


def test_extract_party_terms_drops_suffixes_and_operators():
    terms = extract_party_terms("VTX Communications, LLC AND AT&T Inc.")
    assert "Communications" in terms
    assert "LLC" not in terms
    assert "AND" not in terms


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"ok  {name}")
    print("all query-normalizer tests passed")
