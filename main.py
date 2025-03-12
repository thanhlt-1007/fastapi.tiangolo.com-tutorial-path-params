from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{id}")
async def get_item(id: int):
    return {
        "id": id
    }

@app.get("/users/me")
async def get_me():
    return {
        "id": "Current User"
    }

@app.get("/users/{id}")
async def get_user(id: int):
    return {
        "id": id
    }
