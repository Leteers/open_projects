# -*- coding:utf-8 -*-

from fastapi import FastAPI, Request, Form, Cookie
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Union
from lib import database
import starlette.status as status
# ! - проверить

'''
'''
app = FastAPI()
templates=Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/",response_class=HTMLResponse)
async def home(request : Request, action: str = ''):
        return templates.TemplateResponse('/index.html', {'form': 'register', 'error': '', 'login': '','request': request})

@app.post("/",response_class=HTMLResponse)
async def home_post(request : Request, login: str = Form(), password: str = Form()):
    print(login,password)
    return None
@app.get("/register")
async def registration(request: Request):
    return templates.TemplateResponse('/register.html',{'request': request})