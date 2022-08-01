from datetime import datetime

def cronjob():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    print("Cron job is running")
    print("Tick! The time is: %s" % datetime.now())


# Package Scheduler.

from apscheduler.schedulers.background import BackgroundScheduler

# Main cronjob function.
from main import cronjob

# Create an instance of scheduler and add function.
scheduler = BackgroundScheduler()
scheduler.add_job(cronjob, "interval", seconds=30)

scheduler.start()