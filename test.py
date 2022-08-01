import time
from datetime import datetime

# Package Scheduler.
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler()


def tick():
    print('Tick! The time is: %s' % datetime.now())

def main():
    sched.add_job(tick, 'interval', seconds=30)
    sched.start()

    try:
        while True:
            print(input("Press Enter to submit a job"))
    except (KeyboardInterrupt, SystemExit):
        sched.shutdown()

if __name__ == '__main__':
    main()