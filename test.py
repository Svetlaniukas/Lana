from calendar import calendar
from datetime import datetime

from flask import Flask, render_template

app = Flask (__name__)
@app.route ('/staff')
def staff():
    today = datetime.now ( )
    c = calendar.TextCalendar ( )
    file = open ("staff_week_day.txt", 'r')
    file = open ("staff.weekend.txt", 'r')
def staff_shift( file_week_day, file_weekend):
    staff_dictionary = dict (zip (file_week_day, file_weekend))
    for lines in staff_dictionary :
        (key, val) = lines.split(':')
        staff_dictionary [key] = val

        page_content = render_template (
        "staff.html",
        current_time_and_date = staff_dictionary

    )

    return page_content

if __name__ == "__main__":
    app.run (debug=True)
    
