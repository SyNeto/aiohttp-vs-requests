import aiohttp
import requests

from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    app.requests_session = requests.Session()
    app.aiohttp_session = aiohttp.ClientSession()

@app.on_event("shutdown")
async def shutdown_event():
    await app.aiohttp_session.close()


@app.get('/requests_api')
async def requests_api():
    r = app.requests_session.get('http://localhost:8000/user/?id=001')
    return r.json()

@app.get('/aiohttp_api')
async def aiohttp_api():
    async with app.aiohttp_session.get('http://localhost:8000/user/?id=001') as r:
        return await r.json()
