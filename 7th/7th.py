from datetime import datetime
def datetime_ex():
    delta = datetime.now() - datetime(1994,9,5)
    days = delta.days
    seconds = int(delta.total_seconds())
    minutes = int(seconds/60)
    hours = int(seconds/3600)
    print("It has been {0} days, {1} hours, {2} minutes, {3} seconds since the moment you were born" .format(days,hours,minutes,seconds))
datetime_ex()