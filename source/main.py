from typing import Optional
import sr_api
from fastapi import FastAPI

__version__ = "0.0.1"
api = FastAPI()

client = sr_api.Client()


@api.get("/")
def read_root():
    return {
        "Welcome to": "OofAPI",
        "Made with": "FastAPI",
        "FastAPI": "https://fastapi.tiangolo.com",
        "Copyright 2021": "OofChair https://oofchair.xyz",
        "Version": __version__,
    }


@api.get("/dog")
async def dog_fact():
    fact = await client.get_fact("dog")
    image = await client.get_image("dog")
    return {"fact": fact, "image": image}
