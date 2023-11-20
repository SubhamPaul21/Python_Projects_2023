import requests

params = {"q": "pizza"}
base_url = "https://www.google.com/search"

request = requests.get(base_url, params=params)

print("Status Code:", request.status_code)
print("Creating html file from fetched data...")

search_html_file = open("./pizza_query_fetch.html", "w+")

search_html_file.write(request.text)
