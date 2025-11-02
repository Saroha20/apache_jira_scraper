import json
from src.transformer import humanize_issue

#  Choose which file to process
INPUT_FILE = "data/hadoop_issues.json"
OUTPUT_FILE = "data/hadoop_llm.jsonl"

def load_issues(path):
    """Load Jira issues from JSON file"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_jsonl(records, path):
    """Save records to JSONL file"""
    with open(path, "w", encoding="utf-8") as f:
        for record in records:
            json.dump(record, f, ensure_ascii=False)
            f.write("\n")

def main():
    issues = load_issues(INPUT_FILE)
    print(f"Loaded {len(issues)} issues from {INPUT_FILE}")

    records = []
    for i, issue in enumerate(issues, start=1):
        try:
            rec = humanize_issue(issue)
            records.append(rec)
            if i % 500 == 0:
                print(f" Processed {i} issues...")
        except Exception as e:
            print(f"⚠️ Skipped issue #{i} due to error: {e}")

    save_jsonl(records, OUTPUT_FILE)
    print(f"🎉 Saved {len(records)} records to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
