# Домашнее задание по теме "Модели данных Pydantic".

from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    age: int


app = FastAPI()
users = []


@app.get("/users")
async def get_users() -> list:
    return users


@app.post("/user/{username}/{age}")
async def post_user(user: User) -> User:
    user.id = len(users) + 1
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int,
                      username: str = Path(min_length=5, max_length=20,
                                           description="Enter username", example='UrbanUser'),
                      age: int = Path(ge=18, le=120, description="Enter age", example=24)) -> User:
    try:
        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
            return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", example=99)) -> str:
    try:
        for user in users:
            if user.id == user_id:
                temp = users.pop(user_id)
                return temp
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')
