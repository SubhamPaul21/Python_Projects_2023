from bs4 import BeautifulSoup
import requests
import simplejson as json
from PIL import Image
from io import BytesIO

search_term = input("Input search term: ")
params = {"q": search_term}
base_url = "https://www.bing.com"

request = requests.get(base_url + "/images/search", params=params)

soup = BeautifulSoup(request.text, "html.parser")
links = soup.findAll("div", {"class": "infopt"})
# print("Links: ", links)

for index, link_item in enumerate(links):
    # print(index)
    print("Link Item: ", link_item)
    try:
        image_link = link_item.find("a", {"class": "inflnk"}).attrs['href']
        # print("links: ", image_link)
        img_obj = requests.get(base_url + image_link)
        print("Getting", img_obj.url)
        img_soup = BeautifulSoup(img_obj.content, "html.parser")
        actual_img_obj = img_soup.find("div", {"id": "b_content"})
        img_attrs = actual_img_obj.find("div").attrs["data-firstimg"]
        img_attrs_json = json.loads(img_attrs)
        final_img_url = img_attrs_json["thumbnailUrl"]
        try:
            final_img_obj = requests.get(final_img_url)
            image = Image.open(BytesIO(final_img_obj.content))
            print(image.format)
            image.save("./files/" + search_term + str(index) + "." + image.format)
        except Exception as e:
            print("Exception", e)
            print("Couldn't download image")
    except Exception as e:
        print("Exception", e)
        print("Couldn't parse image DOM")
