from fastapi import FastAPI
from methods.DB_build_helper import *
from fastapi import Request


app = FastAPI()

# PASSWORD = ''

@app.get('/')
async def root(request: Request):
    return {'message': "Welcome to the Spelling Bee FastAPI"}

# @app.get('/password/{password}')
# async def get_new_pass(password: str):
#     global PASSWORD 
#     PASSWORD = password
#     return f'Password updated'

@app.get('/db_update')#/{password}')
async def db_update():#password: str):
    # global PASSWORD
    # if password == PASSWORD:    
        c = Word_Items()
        return(c.update_db())