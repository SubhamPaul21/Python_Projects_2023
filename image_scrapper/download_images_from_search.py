# Import required libraries
import os.path

from bs4 import BeautifulSoup
import requests
import simplejson as json
from PIL import Image
from io import BytesIO

search_term = input("Input search term: ")  # Input term to be taken as search query
params = {"q": search_term}  # params variable to be added to the request get method
base_url = "https://www.bing.com"  # base url for the image download link

request = requests.get(base_url + "/images/search", params=params)  # get the response using the url and params

soup = BeautifulSoup(request.text, "html.parser")  # construct a bs4 object with the response text as a HTML
links = soup.findAll("div", {"class": "infopt"})  # find all div's with class "infopt" in the DOM structure
# of the response text
# print("Links: ", links)

# If files folder doesn't exist --> create a new folder before saving the images in it
if not os.path.isdir("./files/"):
    os.mkdir("./files/")

# If folder doesn't exist with the search query name --> create a new folder before saving the images in it
if not os.path.isdir("./files/" + search_term):
    os.mkdir("./files/" + search_term)


# Create a function to loop through all the pages of image search
def download_images():
    # Iterate through each element in the links list to fetch the required contents
    for index, link_item in enumerate(links):
        # print(index)
        print("Link Item: ", link_item)
        # Use try-catch block to handle exceptions
        try:
            # In each link element, find the anchor with class inflnk. On success, fetch the href attrs from it
            image_link = link_item.find("a", {"class": "inflnk"}).attrs['href']
            # print("links: ", image_link)
            # Append the href link with base url and send a GET request to fetch Response
            img_obj = requests.get(base_url + image_link)
            print("Getting", img_obj.url)
            # Create another bs4 object from the content of the Response as a HTML
            img_soup = BeautifulSoup(img_obj.content, "html.parser")
            # On Success, Find the div which has id of b_content from the bs4 object
            actual_img_obj = img_soup.find("div", {"id": "b_content"})
            # On success, Find div and fetch its data-firstimg attrs to be stored in a variable
            img_attrs = actual_img_obj.find("div").attrs["data-firstimg"]
            # This variable is a dict in a string format, so we use json loads to convert it to dict for processing
            img_attrs_json = json.loads(img_attrs)
            # Finally, get the value of the thumbnailUrl key which is our final img link
            final_img_url = img_attrs_json["thumbnailUrl"]
            # Use try-catch block to handle exceptions during downloading of images
            try:
                # Execute GET request on the final img link
                final_img_obj = requests.get(final_img_url)
                # Handle the response of the content in bytes using BytesIO library and pass it to Pillow library
                # for processing as an Image
                image = Image.open(BytesIO(final_img_obj.content))
                print(image.format)
                # Save the image in its respective folder name based on query by user
                image.save("./files/" + search_term + "/" + search_term + str(index) + "." + image.format)
            except Exception as e:
                print("Exception", e)
                print("Couldn't download image")
        except Exception as e:
            print("Exception", e)
            print("Couldn't parse image DOM")
    download_images()


download_images()
