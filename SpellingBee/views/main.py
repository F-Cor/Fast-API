from SpellingBee import app
from SpellingBee.methods.DB_build_helper import *
from fastapi import Request

PASSWORD = ''

@app.get('/')
async def root(request: Request):
    return {'message': "Welcome to the Spelling Bee FastAPI"}

@app.get('/password/{password}')
async def get_new_pass(password: str):
    global PASSWORD 
    PASSWORD = password
    return f'Password updated'

@app.get('/db_update/{password}')
async def db_update(password: str):
    if password == PASSWORD:    
        c = Word_Items()
        return(c.update_db())