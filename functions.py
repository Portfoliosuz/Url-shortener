import requests
import json
import  config
def get_url(url_):
    try:
        url = f"https://cutt.ly/api/api.php?key={config.api_key}&short={url_}"
        r = requests.get(url)
        result_url = json.loads(r.text)["url"]["shortLink"]
        return result_url
    except:
        return "Limit: 6r/60s !!!"
