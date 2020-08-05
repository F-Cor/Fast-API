import uvicorn

if __name__ == '__main__':
    uvicorn.run('SpellingBee:app', host='localhost', port=5700, reload=True, workers=24)