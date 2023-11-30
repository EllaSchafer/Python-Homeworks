from datetime import datetime as dt
from datetime import time
import calendar

def current_day(cur_date):
    time = dt.today()
    day_week = time.weekday()
    weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    print(weekdays[day_week])
    return weekdays[day_week]

def next_birthday(cur_birthday):
    """
    we are assuming that everyone is born at midnight(00:00:00)
    """
    time = dt.now()
    date = dt.today()
    if '-' in str(cur_birthday):
        birthday = dt.strptime(str(cur_birthday),"%m-%d-%Y")
    elif '/' in str(cur_birthday):
        birthday = dt.strptime(str(cur_birthday),"%m/%d/%Y")
    elif "." in str(cur_birthday):
        birthday = dt.strptime(str(cur_birthday),"%m.%d.%Y")
    else:
        birthday = dt.strptime(str(cur_birthday),"%m%d%Y")
    age = time.year - birthday.year
    if birthday.month > time.month and birthday.day > time.day: # if they are born later in the year
        age -= 1
        diff = dt(date.year, birthday.month, birthday.day, birthday.hour,birthday.minute,birthday.second) - date
        
    else:
        diff = dt(date.year+1, birthday.month, birthday.day, birthday.hour,birthday.minute,birthday.second) - date 
    hr = diff.seconds //(60*60)
    minutess = diff.seconds // 60 -hr *60
    secondss = diff.seconds - hr*60*60 -minutess*60
    print('you are', age, "years old", "your birthday is", diff.days, " days", hr, "hrs", minutess, "minutes and", secondss,"seconds away")
    return diff
print(next_birthday('10102004'))