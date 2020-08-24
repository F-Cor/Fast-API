# Word Bank Fast-API

## Usage (Production)

Hit endpoint to get word list, letter list, must use letter, and word list length
Endpoint: `https://git.heroku.com/word-bank-db.git/db_pull`

## Usage (development)

Clone the repo, then run the following cli command within the repo directory

```
$ pipenv install
$ pipenv shell
$ pipenv run run.py
```

In the cli you should see:
```
INFO:     Uvicorn running on http://localhost:5700 (Press CTRL+C to quit)
INFO:     Started reloader process [5212] using statreload
INFO:     Started server process [14560]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Follow the link to `http://localhost:5700`

From there you can access the swagger ui to test the i/o by going to `http:localhost:5700/docs`
