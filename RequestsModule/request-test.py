import requests

r = requests.get("https://google.com")
print("status:", r.status_code)
print(r.url)

f = open("./page.html", "w+")
f.write(r.text)
