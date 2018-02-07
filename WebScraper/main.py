from bs4 import BeautifulSoup
import requests

search = input("Enter search term:")
params = {"q": search}
r = requests.get("http://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]
    children = item.children
    for child in children:
        print(child)

    # if item_text and item_href:
        # print(item_text)
        # print(item_href)
        # print(item.find("div", {"class":"b_caption"}).find("p").text)
        # print("Summary:", item.find("a").parent.parent.find("p").text)

