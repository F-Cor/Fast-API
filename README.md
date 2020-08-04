# Fast-API

# TODO:
- [x] Postgres  
    - New table for each user?
    - Store full wordbank in db?
- [ ] Define i/o of each step  
- [ ] Convert old py files to methods in fastapi app
    - [x] For database updates
    - [ ] For interacting with front end
- [ ] Security for DB updates? (easy to hit endpoint to update)
- [ ] Migrate from local -> Heroku
- [ ] Look into 12hour timer for reset 
    - background tasks?
- [ ] Look into Psycopg2
    - Update database every x hours
    - Update user info when they submit

Maybe we only use this to update the DB, then all other interactions are handled between
front end and DB?