"""Standalone unit tests for us_citation_patterns.

Run with: pytest, or `python -m pytest tests/`, from the repo root.
Stdlib only, no external dependencies.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from citations.us_citation_patterns import looks_like_us_citation  # noqa: E402


def test_federal_statute_citation():
    assert looks_like_us_citation("See 15 U.S.C. 78j(b) for the standard.")


def test_cfr_citation():
    assert looks_like_us_citation("The rule is at 29 C.F.R. 1604.11.")


def test_us_reports_case_citation():
    assert looks_like_us_citation("Brown v. Board, 347 U.S. 483.")


def test_state_reporter_citation():
    assert looks_like_us_citation("Cited 16 Cal.App.4th 943 on the point.")


def test_case_caption():
    assert looks_like_us_citation("The holding in Marbury v. Madison controls.")


def test_plain_prose_is_not_a_citation():
    assert not looks_like_us_citation("Please summarize the meeting notes.")


def test_empty_and_none_are_false():
    assert not looks_like_us_citation("")
    assert not looks_like_us_citation(None)


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"ok  {name}")
    print("all citation tests passed")
