from fastapi import FastAPI
from enum import Enum

class UserName(str, Enum):
    ALEXNET = "alexnet"
    RESNET = "resnet"
    LENET = "lenet"

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

@app.get("/users/name/{name}")
async def get_user_by_name(name: UserName):
    message = "Have some residuals"

    if name is UserName.ALEXNET:
        message = "Deep Learning FTW!"

    if name.value == "resnet":
        message = "LeCNN all the image"

    return {
        "name": name,
        "message": message,
    }
