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
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def start_page_get(request: Request):
    return templates.TemplateResponse('login.html', {'form': 'register', 'error': '', 'login': '', 'request': request})


@app.post("/login", response_class=HTMLResponse)
async def login_post(request: Request, login: str = Form(), password: str = Form()):
    conn = database.Connection()
    if(conn.check_auth(login, password)):
        response = RedirectResponse('/home', status_code=302)
        response.set_cookie(key='login',value='login')
        return response
    else:
        return templates.TemplateResponse('/login.html', context={'request': request, 'error': 'wrong'})


@app.post("/", response_class=HTMLResponse)
async def start_page_post(request: Request, login: str = Form(), password: str = Form()):
    conn = database.Connection()
    if(conn.check_auth(login, password)):
        response = RedirectResponse('/home', status_code=302)
        response.set_cookie(key='login',value='login')
        return response
    else:
        return templates.TemplateResponse('/login.html', context={'request': request, 'error': 'wrong'})


@app.get("/register", response_class=HTMLResponse)
async def registration_get(request: Request):
    return templates.TemplateResponse('/register.html', {'request': request})


@app.post("/registr_success", response_class=HTMLResponse)
async def registration_post(request: Request, login: str = Form(), password: str = Form()):
    conn = database.Connection()
    user = conn.create_user(login, password)
    if(user == True):
        return templates.TemplateResponse('/login.html', {'error': 'success', 'request': request})
    else:
        return templates.TemplateResponse('/register.html', context={'error': user, 'request': request})

@app.get('/home',response_class=HTMLResponse)
async def home_page_get(request: Request, login : str = Cookie(None)):
    return templates.TemplateResponse('/home_page.html',{'request':request})