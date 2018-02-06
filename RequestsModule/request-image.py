import requests
from io import BytesIO
from PIL import Image

# r = requests.get("https://wallpapercave.com/wp/Jzn5hwl.jpg")
r = requests.get("http://www.qygjxz.com/data/out/75/4030693-epic-wallpaper.png")

print("status code:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)

path = "./image." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save iamge.")