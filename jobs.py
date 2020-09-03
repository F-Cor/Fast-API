from apscheduler.schedulers.blocking import BlockingScheduler
from methods.db_utils import db_updater, del_table

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='0-6', hour='0, 12', timezone='UTC')
def update_database():
    db_updater()
    
@sched.scheduled_job('cron', day_of_week='0-6', hour='0, 12', minute='2', timezone='UTC')
def delete_old_table():
    del_table()

sched.start()