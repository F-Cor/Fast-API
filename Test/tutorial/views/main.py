from tutorial import app, templates
from fastapi import Request

@app.get('/')
async def root(request: Request):
    return templates.TemplateResponse('base.html', {'request': request})

@app.get('/tutorial')
async def tutorial():
    '''
    This is a tutorial function, to use this run curl http://localhost:5700/tutorial
    '''
    return {'message': {"this is another route"}}