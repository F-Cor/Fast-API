from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from methods.db_utils import db_updater
from sqlalchemy import create_engine
import os
import pandas as pd

DB_URL = os.environ['DATABASE_URL']
engine = create_engine(DB_URL)

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='0-6', hour='0, 12', timezone='UTC')
def update_database():
    db_updater()

sched.start()