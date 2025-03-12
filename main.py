from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{id}")
async def get_item(id: int):
    return {
        "id": id
    }
