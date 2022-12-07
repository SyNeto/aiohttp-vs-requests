from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def user(id: str):
    return {'id': id}