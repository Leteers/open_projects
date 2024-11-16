from datetime import datetime, timedelta
from typing import Annotated, Union

from fastapi import FastAPI, Request, Form, Cookie, File, Response, Body, UploadFile, BackgroundTasks, HTTPException, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.post('/block_transactions')
def block_transactions(request: Request, transaction_id: int, from_user_id: int, to_user_id: int, amount: int, block_type: str):
    return 200
@app.post('/unblock_transactions')
def block_transactions(request: Request, user_id: int):
    return 200
@app.post('/is_blocked')
def is_blocked(request: Request, user_id: int) -> bool:
    if user_id ==1:
        return True
    else:
        return False
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)