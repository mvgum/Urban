# Домашнее задание по теме "Основы Fast Api и маршрутизация".
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_page():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def read_adm():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def read_user(user_id):
    return {f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def read_name(username, age):
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
