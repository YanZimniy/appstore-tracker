# fetch_apps.py
import requests
import json
from datetime import datetime

# RSS URL Apple
APPLE_RSS = "https://rss.apple.com/api/v1/us/ios-apps/top-free/all/200/explicit.json"

# Прокси rss2json (заменяет Apple RSS)
PROXY_URL = f"https://api.rss2json.com/v1/api.json?rss_url={APPLE_RSS}"

def get_top_apps():
    response = requests.get(PROXY_URL)
    response.raise_for_status()
    data = response.json()
    apps = []

    for item in data.get("items", []):
        apps.append({
            "name": item.get("title"),
            "id": item.get("guid"),
            "link": item.get("link"),
        })
    return apps

def save_to_file(apps):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"top_apps_{today}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(apps, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(apps)} apps to {filename}")

if __name__ == "__main__":
    apps = get_top_apps()
    save_to_file(apps)
