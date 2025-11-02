# tests/test_transformer.py
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.transformer import humanize_issue


def test_humanize_basic():
    # Minimal synthetic Jira issue with summary, description and comments
    issue = {
        "fields": {
            "summary": "Test issue summary",
            "description": "This is a test description. It contains details.\nAnd a newline.",
            "comment": {
                "comments": [
                    {"body": "First comment line\nSecond line"},
                    {"body": "Another comment"}
                ]
            }
        }
    }

    rec = humanize_issue(issue)

    # Basic structure checks
    assert isinstance(rec, dict)
    assert "instruction" in rec
    assert "input" in rec
    assert "output" in rec

    # Content checks: title and description should appear in input
    assert "Test issue summary" in rec["input"]
    assert "This is a test description" in rec["input"]

    # Comments combined should appear in input (at least part of them)
    assert "First comment line" in rec["input"] or "Another comment" in rec["input"]
