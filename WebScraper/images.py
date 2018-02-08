from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import requests

search = input("Search for:")
params = {"q": search}
r = requests.get("http://www.bing.com/images/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")

links = soup.findAll("a", {"class": "thumb"})
print(len(links))
for item in links:
    print(item)
    img_obj = requests.get(item.attrs["href"])
    print("Getting:", item.attrs["href"])
    title = item.attrs["href"].split("/")[-1]
    print("Title:", title)
    try:
        img = Image.open(BytesIO(img_obj.content))
        img.save("./scraped_impages/" + title, img.format)
    except IOError:
        print("Cannot save iamge.")
