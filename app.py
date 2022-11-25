import calendar
from datetime import datetime
from _CAL.Holiday import today
from flask import Flask, render_template


app = Flask (__name__)

@app.route ('/')
@app.route ('/home')
def home():
        date_time = datetime.now ( )
        calendar_year = calendar.TextCalendar ( )
        page_content = render_template ("home.html",
                       current_time = today.year,
                       calendar_year = calendar_year.formatyear (2002, w=2, l=1, c=6, m=3)

                                        )
        return page_content


def read_staff_from_file():
    dict_staff = {}
    for_week_days_shift = open ("staff_week_day.txt", 'r')
    for_staff_weekend_shift = open ("staff_weekend.txt", 'r')
    for line in for_week_days_shift:
        (key, val) = line.split (':')
        dict_staff[key] = val
    for line in for_staff_weekend_shift:
        (key, val) = line.split ('=')
        dict_staff[key] = val

        return

@app.route ('/staff')
def staff(dict_staff):
         for_staff_weekend_shift = read_staff_from_file()
         for_week_days_shift = read_staff_from_file()
         page_content = render_template ("staff.html",
                        for_week_days_shift = for_week_days_shift,
                        for_staff_weekend_shift = for_staff_weekend_shift
                                         )


         return page_content


if __name__ == "__main__":
         app.run (debug=True)
        
