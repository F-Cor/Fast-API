from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from methods.db_utils import check_db
import os

app = FastAPI()

origin = os.getenv("LOCAL_ORIGIN")
vercel = os.getenv("VERCEL")

origins = [
    origin,
    vercel
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
    return {'message': "Welcome to the Word Bank FastAPI"}

@app.get('/db_pull')
async def db_pull():
    return check_db()
