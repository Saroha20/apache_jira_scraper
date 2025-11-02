import requests
import json
from time import sleep
from tenacity import retry, stop_after_attempt, wait_exponential

BASE_URL = "https://issues.apache.org/jira/rest/api/2/search"

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=2, max=10))
def fetch_issues(project_key, start=0, max_results=50):
    """
    Fetch a batch of issues from a Jira project.
    """
    params = {
        "jql": f"project={project_key}",
        "startAt": start,
        "maxResults": max_results,
        "fields": "summary,status,priority,assignee,reporter,created,updated,labels,description,comment"
    }

    response = requests.get(BASE_URL, params=params, timeout=20)

    if response.status_code == 429:
        print("Rate limited — sleeping for 30 seconds...")
        sleep(30)
        return fetch_issues(project_key, start, max_results)

    response.raise_for_status()
    return response.json()


def scrape_project(project_key):
    """
    Fetch all issues for a given project, handling pagination.
    """
    print(f"\n Starting scrape for project: {project_key}")
    all_issues = []
    start_at = 0
    max_results = 50

    while True:
        print(f"Fetching issues {start_at}–{start_at + max_results}...")
        data = fetch_issues(project_key, start=start_at, max_results=max_results)
        issues = data.get("issues", [])
        if not issues:
            break
        all_issues.extend(issues)

        if len(issues) < max_results:
            break  # no more pages
        start_at += max_results

    output_path = f"data/{project_key.lower()}_issues.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_issues, f, indent=2, ensure_ascii=False)

    print(f" Saved {len(all_issues)} total issues to {output_path}")


if __name__ == "__main__":
    
    projects = ["HADOOP", "SPARK", "KAFKA"]

    for project in projects:
        scrape_project(project)
