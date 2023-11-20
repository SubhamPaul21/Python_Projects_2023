import requests

request = requests.get("https://waander.in/")
print("Status:", request.status_code)
print("Details:", request.text)

html_file = open("./waander_homepage.html", "w+")
html_file.write(request.text)
