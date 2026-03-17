import requests
import time
import json

def get_top_apps(retries=3, delay=5):
    url = "https://api.rss2json.com/v1/api.json?rss_url=https://rss.apple.com/api/v1/us/ios-apps/top-free/all/200/explicit.json"
    
    for attempt in range(1, retries+1):
        try:
            response = requests.get(url)
            response.raise_for_status()
            print("Apps fetched successfully")
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < retries:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("All attempts failed. Returning None.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None

def save_report(data, filename="report.json"):
    if data is None:
        print("No data to save.")
        return
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Report saved to {filename}")

if __name__ == "__main__":
    apps = get_top_apps()
    save_report(apps)
