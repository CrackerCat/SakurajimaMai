import os
import time

SECRET = os.getenv('SECRET')
WEBHOOK = os.getenv('WEBHOOK')

WB_UIDS = os.getenv('WB_UIDS').split(',')if os.getenv('WB_UIDS') is not None else ''
bIds = os.getenv('BIDS').split(',')if os.getenv('BIDS') is not None else ''


breakfast = os.getenv('BREAKFAST')
if breakfast is not None and breakfast != '':
    breakfast = (
        time.strptime(breakfast, '%H') if len(breakfast) == 2 else time.strptime(
            breakfast, '%H%M'))

lunch = os.getenv('LUNCH')
if lunch is not None and lunch != '':
    lunch = (
        time.strptime(lunch, '%H') if len(lunch) == 2 else time.strptime(
            lunch, '%H%M'))

dinner = os.getenv('DINNER')
if dinner is not None and dinner != '':
    dinner = (
        time.strptime(dinner, '%H') if len(dinner) == 2 else time.strptime(
            dinner, '%H%M'))