from SpellingBee import app, templates
from fastapi import Request

@app.get('/')
async def root(request: Request):
    return templates.TemplateResponse('base.html', {'request': request})

@app.get('/input/{name}')
async def input(name: str):
    return {'message': f'Hello {name}, welcome to the SpellingBee FastAPI'}