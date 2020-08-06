from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from methods.DB_build_helper import *

app = FastAPI()
# PASSWORD = ''

origins = [
    'http://localhost:3000'
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

# @app.post('/password')
# async def get_new_pass(password: str):
#     global PASSWORD 
#     PASSWORD = password
#     return f'Password updated to {password}'

@app.get('/db_update')
async def db_update():#password: str):
    # global PASSWORD
    # if password == PASSWORD:    
        c = Word_Items()
        return(c.update_db())