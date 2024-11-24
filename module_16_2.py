# Домашнее задание по теме "Валидация данных".
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/user/{user_id}")
async def read_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", example=99)):
    return {f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def read_name(username: str = Path(min_length=5, max_length=20,
                                         description="Enter username", example='UrbanUser'),
                    age: int = Path(ge=18, le=120, description="Enter age", example=24)):
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
