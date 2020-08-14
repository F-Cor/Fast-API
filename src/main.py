from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from methods.DB_build_helper import *
import os

app = FastAPI()
load_dotenv()
origin = os.getenv("ORIGINS")

origins = [
    origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

@app.get('/')
async def root(request: Request):
    return {'message': "Welcome to the Spelling Bee FastAPI"}

@app.get('/db_update')
async def db_update():
    c = Word_Items()
    return(c.update_db())