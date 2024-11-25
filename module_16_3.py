# Домашнее задание по теме "CRUD Запросы: Get, Post, Put, Delete".
from fastapi import FastAPI, Path


app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def post_user(username: str = Path(min_length=5, max_length=20,
                                         description="Enter username", example='UrbanUser'),
                    age: int = Path(ge=18, le=120, description="Enter age", example=24)) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int,
                      username: str = Path(min_length=5, max_length=20,
                                         description="Enter username", example='UrbanUser'),
                      age: int = Path(ge=18, le=120, description="Enter age", example=24)) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} has been updated"


@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", example=99)) -> str:
    users.pop(user_id)
    return f"The user {user_id} has been deleted"
