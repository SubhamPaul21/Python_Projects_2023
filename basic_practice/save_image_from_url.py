import requests
from PIL import Image
from io import BytesIO


request = requests.get("https://img.freepik.com/free-photo/autumn-leaf-falling-revealing-intricate-leaf-vein"
                       "-generated-by-ai_188544-9869.jpg?w=1060&t=st=1700472193~exp=1700472793~hmac"
                       "=059d81ad42bf983f6b0640548ef286ea4c3c29922bb5f1447d64e58a12ff3ecc")

print("Status Code:", request.status_code)

image = Image.open(BytesIO(request.content))

file_name = "./hd_image." + image.format

try:
    image.save(file_name, image.format)
except IOError:
    print("Couldn't save the image")
