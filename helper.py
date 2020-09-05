import yaml
import uuid
import datetime
import calendar
import time
from datetime import datetime, timedelta, date


def epoch_time():
    return calendar.timegm(time.gmtime())


def past_calc(time_check):
    now_time = epoch_time()
    thirty_days_ago = now_time - (((60 * 60) * 24) * 30)
    if time_check > thirty_days_ago:
        return True
    else:
        return False

def client_check(key,clients):
    if key in clients:
        if past_calc(clients[key]):
            return True

    return False