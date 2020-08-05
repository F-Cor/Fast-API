import uvicorn

if __name__ == '__main__':
    uvicorn.run('src.main:app', host='localhost', port=5700, reload=True, debug=True, workers=24)