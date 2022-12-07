import calendar
from datetime import datetime

import items as items
from _CAL.Holiday import today
from flask import Flask, render_template


app = Flask (__name__)

@app.route ('/')
@app.route ('/home')
def home():
    date_time = datetime.now ( )
    calendar_year = calendar.TextCalendar ( )
    page_content = render_template ("home.html",
    current_time = date_time ,
    calendar_year = calendar_year.formatyear(format())

    return page_content


def read_staff_from_file(file_name,file_delemiter):
    dict_staff = {}
    for_week_days_shift = open (file_name ,'r')
    for line in for_week_days_shift:
        (key, val) = line.split(file_delemiter)
        dict_staff[key] = val
    return dict_staff

@app.route ('/staff')
def staff():
         for_week_days_shift = read_staff_from_file ("staff_week_day.txt", ":")
         for_staff_weekend_shift = read_staff_from_file ("staff_weekend.txt","=")
         page_content = render_template ("staff.html",
                        for_week_days_shift = for_week_days_shift,
                        for_staff_weekend_shift = for_staff_weekend_shift
                                         )
         return page_content
if __name__ == "__main__":
         app.run (debug=True)
        
