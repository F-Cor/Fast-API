from SpellingBee import app, templates
from SpellingBee.methods.DB_build_helper import *
from fastapi import Request

PASSWORD = ''

@app.get('/')
async def root(request: Request):
    return templates.TemplateResponse('base.html', {'request': request})

@app.get('/password/{password}')
async def get_new_pass(password: str):
    global PASSWORD 
    PASSWORD = password
    return {'message': "Password updated",
            'new_pass': {PASSWORD}}

@app.get('/db_update/{password}')
async def db_update(password: str):
    if password == PASSWORD:    
        c = Word_Items()
        c.get_all_words()
        c.get_letters()
        c.get_word_list()
        return({"letter_list": c.letter_list,
                "must_use": c.must_use,
                "word_list": c.word_list})