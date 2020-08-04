from SpellingBee import app, templates
from SpellingBee.methods.DB_build_helper import Word_Items
from fastapi import Request


@app.get('/')
async def root(request: Request):
    return templates.TemplateResponse('base.html', {'request': request})

@app.get('/input/{user}/{word}')
async def input(user: str, word: str):
    '''
    Takes in word, checks DB and returns info to front end
    '''
    # Bunch of stuff to access DB
        # Create table for new user
    # Check if word is acceptable
    # Check if word contains "must_use" letter
    # Check that all letters are in "letters" list
    # Update database with new info
    # Return all info to front end
    
    valid_word = True
    found_words: list = []
    if valid_word:
        found_words.append(word)
    return {'user': user,
            'valid_word': valid_word,
            'found_words': found_words,
            'word': word}

@app.get('/db_update')
async def db_update():
    c = Word_Items()
    c.get_all_words()
    c.get_letters()
    c.get_word_list()
    return({"letter_list": c.letter_list,
            "must_use": c.must_use,
            "word_list": c.word_list})
