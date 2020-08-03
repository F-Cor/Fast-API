from fastapi import Request, status, BackgroundTasks
from fastapi.responses import JSONResponse
from SpellingBee import app, templates


def _update_db(word_list: list, letters: list, must_use: str):
    '''
    Function to create new word list for the day and post to db
    '''
    return None

# @app.post('task/db_update/{word_list}/{letters}/{must_use}')
# async def db_update(word_list: list, letters: list, must_use: str, background_tasks: BackgroundTasks):
#     '''
#     Uses _update_db to create new word_list, letters, and must_use in DB
#     '''
#     background_tasks.add_task(_update_db, word_list, letters, must_use)
#     return {'message': f""}