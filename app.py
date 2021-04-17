from fastapi import FastAPI
from pydantic import BaseModel
from PIL import Image
from imgcompare import image_diff_percent
import requests

class Images(BaseModel):
    image_one: str
    image_two: str

app = FastAPI()

@app.get('/compare/{key}')
async def get(
        images: Images,
        key
        ):
    image_one = image_two = None

    if not authorize_key(key):
        return {'Permission': 'Denied'}

    if "https://" in images.image_one:
        image_one = Image.open(requests.get(images.image_one, stream=True).raw)
    else:
        image_one = Image.open(images.image_one)

    if "https://" in images.image_two:
        image_two= Image.open(requests.get(images.image_two, stream=True).raw)
    else:
        image_two = Image.open(images.image_two)

    diff = 100 - image_diff_percent(image_one, image_two)

    return {'Percentage Comparison': str(diff) + '%' }

def authorize_key(client_key):
    print('hello world')
    file = open('keys.txt', "r")
    key = file.readline()
    while key:
        key = key.replace('\n', '')
        if key == client_key: 
            return True
        key = file.readline()
    return False

