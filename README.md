# Word Bank Fast-API

## Usage (Production)

The app refreshes the Word Bank database updating the possible words list and letters to use for the time period

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
