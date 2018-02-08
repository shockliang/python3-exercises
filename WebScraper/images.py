from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import requests
import os

def start_search():
    search = input("Search for:")
    params = {"q": search}
    dir_name = search.replace(" ","_").lower()

    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    r = requests.get("http://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text, "html.parser")

    links = soup.findAll("a", {"class": "thumb"})
    print(len(links))
    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])
            print("Getting:", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            print("Title:", title)
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./" + dir_name + "/" + title, img.format)
            except IOError:
                print("Cannot save image.")
        except:
            print("Can't request image url")

    start_search()

start_search()
