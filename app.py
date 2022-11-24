import calendar
from datetime import datetime
from _CAL.Holiday import today
from flask import Flask, render_template
from itertools import chain

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
def staff(current_staff_shift):
    staff_week_day = open("staff_week_day.txt", 'r')
    staff_weekend = open ("staff.weekend.txt", 'r')
 
    def items(current_staff_shift ):
        current_staff_shift = dict (chain (staff_week_day .items ( ), staff_weekend.items ( )))

    page_content = render_template ("staff.html",
    current_time_and_date = current_staff_shift,
    )
   
    return page_content


if __name__ == "__main__":
    app.run (debug=True)




   