# -*- coding:utf-8 -*-

from fastapi import FastAPI, Request, Form, Cookie
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Union
import starlette.status as status
import uvicorn
# ! - проверить

'''
'''
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/images",StaticFiles(directory="images"), name="images")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/scripts",StaticFiles(directory="scripts"), name="scripts")


@app.get("/", response_class=HTMLResponse)
async def start_page_get(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
