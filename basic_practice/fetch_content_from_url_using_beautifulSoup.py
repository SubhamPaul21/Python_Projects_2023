from bs4 import BeautifulSoup
import requests

search_term = input("Enter the search term for Google: ")
params = {"q": search_term}
base_url = "https://www.google.com/search"

request = requests.get(base_url, params=params)

soup = BeautifulSoup(request.text, "html.parser")

print(soup.prettify())
