import sr_api
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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
        "Home page": "Coming soon!",
        "Docs": "https://api.pwnbot.xyz/redoc",
    }


@api.get("/api/fact/dog")
async def dog_fact():
    fact = await client.get_fact("dog")
    return {"fact": fact}

@api.get("/api/fact/cat")
async def cat_fact():
    fact = await client.get_fact("cat")
    return {"fact": fact}
