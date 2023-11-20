import simplejson as json
import os

file_path = "./data.json"
if os.path.exists(file_path) and os.path.getsize(file_path) != 0:
    old_file = open(file_path, "r+")
    data = json.loads(old_file.read())
    print("Current Age:", data["age"], "------- Adding 1 more year")
    data["age"] += 1
    print("New Age:", data["age"])
else:
    old_file = open(file_path, "w+")
    data = {"name": "Subham", "age": 26}
    print("No Data found!")
    print("Adding Age:", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))
