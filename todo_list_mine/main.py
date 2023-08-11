# -*- coding:utf-8 -*-

from fastapi import FastAPI, Request, Form, Cookie
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Body
from typing import Union
from lib import database
import starlette.status as status
import uvicorn
import requests
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


class Item(BaseModel):
    make : str

@app.get("/", response_class=HTMLResponse)
async def start_page_get(request: Request):
    return templates.TemplateResponse('login.html', {'form': 'register', 'error': '', 'login': '', 'request': request})


@app.post("/login", response_class=HTMLResponse)
async def login_post(request: Request, login: str = Form(), password: str = Form()):
    conn = database.Connection()
    if(conn.check_auth(login, password)):
        response = RedirectResponse('/home', status_code=302)
        response.set_cookie(key='login',value=login)
        response.set_cookie(key='user_id',value=conn.search_user_id(login))
        return response
    else:
        return templates.TemplateResponse('/login.html', context={'request': request, 'error': 'wrong'})


@app.post("/", response_class=HTMLResponse)
async def start_page_post(request: Request, login: str = Form(), password: str = Form()):
    conn = database.Connection()
    if(conn.check_auth(login, password)):
        response = RedirectResponse('/home', status_code=302)
        response.set_cookie(key='login',value=login)
        response.set_cookie(key='user_id',value=conn.search_user_id(login))
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
    conn = database.Connection()
    return templates.TemplateResponse('/home_page.html',context={'request':request,'todos':conn.get_to_dos(conn.search_user_id(login))})


@app.post('/receiver')
async def postME(payload: Dict[Any, Any], user_id: str = Cookie(None)):
#    data = jsonify(data)
    conn = database.Connection()
    if payload['stat']=='new':
        a=conn.insert_to_do(user_id,payload["text"],payload["stat"])
        return a[0]
    elif payload['stat']=='done':
        conn.update_to_do_status_to_close(payload['id'])
    else:
        pass
if __name__ == "__main__":
    uvicorn.run("main:app", host="37.140.192.188", port=8000, reload=True)