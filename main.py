from typing import Optional
import sr_api
from fastapi import FastAPI

api = FastAPI()

client = sr_api.Client()

@api.get("/")
def read_root():
    return {"Hello": "World"}


@api.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@api.get("/dog")
async def dog_fact():
    fact = await client.get_fact("dog")
    image = await client.get_image("dog")
    return {"fact": fact, "image": image}
