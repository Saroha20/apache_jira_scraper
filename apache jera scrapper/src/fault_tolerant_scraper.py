import json
import os
import requests
import time

JIRA_API = "https://issues.apache.org/jira/rest/api/2/search"
PROJECT = "HADOOP"
OUTPUT_FILE = "data/hadoop_issues.json"
BATCH_SIZE = 50
MAX_RESULTS = 20000

def fetch_issues(start_at=0):
    """Fetch issues from Jira API with retries."""
    params = {
        "jql": f"project={PROJECT}",
        "startAt": start_at,
        "maxResults": BATCH_SIZE,
    }
    for attempt in range(3):
        try:
            resp = requests.get(JIRA_API, params=params, timeout=30)
            if resp.status_code == 200:
                return resp.json().get("issues", [])
            else:
                print(f"⚠️  HTTP {resp.status_code} — retrying...")
        except Exception as e:
            print(f"⚠️  Error: {e} — retrying in 5s...")
            time.sleep(5)
    print(f" Failed to fetch batch starting at {start_at}")
    return []

def save_progress(issues):
    """Save progress to disk."""
    os.makedirs("data", exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(issues, f, indent=2, ensure_ascii=False)

def load_progress():
    """Load previously saved issues if file exists."""
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def main():
    issues = load_progress()
    start_at = len(issues)
    print(f" Resuming from issue #{start_at}")

    while start_at < MAX_RESULTS:
        new_issues = fetch_issues(start_at)
        if not new_issues:
            print(" No new issues fetched, stopping.")
            break

        issues.extend(new_issues)
        save_progress(issues)

        start_at += len(new_issues)
        print(f" Fetched up to {start_at} issues.")
        time.sleep(2)

    print(f" Completed. Total issues saved: {len(issues)}")

if __name__ == "__main__":
    main()
