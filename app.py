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

@app.route ('/staff')
def staff():
    file = open ("staff_week_day.txt", 'r')
    file = open ("staff.weekend.txt", 'r')
    
    for line in file:
        def staff_shift(file_week_day, file_weekend):
            staff_dictionary = dict (zip (file_week_day, file_weekend))
            for lines in staff_dictionary:
                (key, val) = lines.split (':')
                staff_dictionary[key] = val

                page_content = render_template (
                    "staff.html",
                    current_time_and_date = staff_dictionary

                )

    return page_content

if __name__ == "__main__":
    app.run (debug=True)