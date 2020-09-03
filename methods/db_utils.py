from datetime import datetime, timedelta
from methods.word_list_gen import *
from sqlalchemy import create_engine
import os
import pandas as pd

DB_URL = os.environ['DATABASE_URL']
engine = create_engine(DB_URL)

def db_updater():
    '''
    Generates new words, letters, and must use words.
    Creates new table in database and stores these items.
    '''
    today = datetime.today().strftime('%b_%d_%y_%H').lower()
    c = Word_Items()
    c.update_db()
    df = pd.DataFrame({'words': c.word_list, 
                       'letters': c.letter_list + [None]*(len(c.word_list) - len(c.letter_list)),
                       'must_use': [c.must_use]*len(c.word_list),
                       'list_len': [len(c.word_list)]*len(c.word_list)})
    df.to_sql(today, con=engine)

def check_db():
    '''
    Method to return data from the database
    '''
    now = datetime.now().hour
    today = datetime.today().strftime('%b_%d_%y').lower()

    if 0 <= now < 12:
        today += '_00'
    else:
        today += '_12'

    df = pd.read_sql_table(today, con=engine)
    word_list = df['words'].tolist()
    letters = df['letters'][0:7].tolist()
    must_use = df['must_use'][0]
    list_len = len(word_list)

    return {"word_list": word_list,
            "letters": letters,
            "must_use": must_use,
            "list_len": list_len}

def del_table():
    '''
    Deletes a table from 14 days ago (Only keep 2 weeks of tables in the DB)
    '''
    table = (datetime.now() - timedelta(days = 14)).strftime('%b_%d_%y_%H').lower()
    engine.execute(f'DROP TABLE IF EXISTS {table};')