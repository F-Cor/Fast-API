from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory='./SpellingBee/static'), name='static')


from SpellingBee.views import main