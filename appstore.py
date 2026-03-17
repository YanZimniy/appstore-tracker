import requests

# Ссылка на топ 200 бесплатных приложений в US
URL = "https://rss.apple.com/api/v1/us/ios-apps/top-free/all/200/explicit.json"

def get_top_apps():
    response = requests.get(URL)
    data = response.json()
    return data["feed"]["results"]