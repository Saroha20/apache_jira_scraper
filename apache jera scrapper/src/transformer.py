def clean_text(text: str) -> str:
    """
    Basic text cleaning: remove extra spaces, normalize newlines, and strip.
    """
    if not isinstance(text, str):
        return ""
    text = text.replace("\r", " ").replace("\n", " ").strip()
    text = " ".join(text.split())  # collapse multiple spaces
    return text

def humanize_issue(issue: dict) -> dict:
    """
    Transform a raw Jira issue dictionary into a structured, clean record
    with instruction, input, and output fields for LLM training.
    """
    fields = issue.get("fields", {})
    summary = clean_text(fields.get("summary", ""))
    description = clean_text(fields.get("description", ""))
    comments = fields.get("comment", {}).get("comments", [])

    comment_texts = []
    for i, c in enumerate(comments, start=1):
        body = clean_text(c.get("body", ""))
        if body:
            comment_texts.append(f"Comment {i}: {body}")

    combined_comments = " ".join(comment_texts)

    # Combine all relevant text as input context
    input_text = f"Issue: {summary}. Description: {description}. {combined_comments}"

    # Create final structured record (LLM-ready)
    record = {
        "id": issue.get("key", ""),
        "project": fields.get("project", {}).get("key", ""),
        "status": fields.get("status", {}).get("name", ""),
        "priority": fields.get("priority", {}).get("name", ""),
        "reporter": fields.get("reporter", {}).get("displayName", ""),
        "title": summary,
        "instruction": "Summarize the following software issue and its discussion.",
        "input": input_text,
        "output": f"This issue is about: {summary}. It involves: {description[:150]}..."
    }

    return record
