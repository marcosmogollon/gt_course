#!/usr/bin/env python3

from datetime import date

def get_todays_date():
    current_day = (str(date.today().day))
    current_month = (str(date.today().month))
    current_year = (str(date.today().year))
    return current_year + "/" + current_month + "/" + current_day

print(get_todays_date())
