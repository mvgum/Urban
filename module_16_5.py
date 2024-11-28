# Домашнее задание по теме "Модели данных Pydantic".
from fastapi import FastAPI, Path, HTTPException, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory='templates')


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = []


@app.get("/", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/user/{user_id}')
async def get_user(request: Request, user_id: int):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail='User was not found')


@app.post("/user/{username}/{age}", response_class=HTMLResponse)
async def post_user(request: Request,
                    username: str = Path(min_length=5, max_length=20,
                                         description="Enter username", example='UrbanUser'),
                    age: int = Path(ge=18, le=120, description="Enter age", example=24)):
    user = User(id=len(users) + 1, username=username, age=age)
    users.append(user)
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.put("/user/{user_id}/{username}/{age}", response_class=HTMLResponse)
async def update_user(request: Request,
                      user_id: int = Path(ge=1),
                      username: str = Path(min_length=5, max_length=20),
                      age: int = Path(ge=18, le=120)):
    try:
        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
            return templates.TemplateResponse("users.html", {"request": request, "users": users})
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}', response_class=HTMLResponse)
async def delete_user(request: Request,
                      user_id: int = Path(ge=1, le=100)):
    try:
        for user in users:
            if user.id == user_id:
                users.remove(user)
                return templates.TemplateResponse("users.html", {"request": request, "users": users})
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')
