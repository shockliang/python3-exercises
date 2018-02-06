import requests
import json


url = "https://www.googleapis.com/urlshortener/v1/url"
payload = {"longUrl": "https://www.googleapis.com/urlshortener/v1/url"}

headers = {"Content-Type": "application/json"}
r = requests.post(url, json=payload, headers=headers)

# print(json.loads(r.text))
print(r.text)
