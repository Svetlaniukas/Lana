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


         return page_content


for_week_days_shift = open ("staff_week_day.txt", 'r')
for_staff_weekend_shift = open ("staff.weekend.txt", 'r')
staff_file = {}
@app.route ('/staff')
def staff(staff_weekend=None, staff_week_day=None):
         today = datetime.now ( )
         for line in staff_weekend:
             (key, val) = line.split ('=')
         for line in staff_week_day:
             (key, val) = line.split (':')
         page_content = render_template ("staff.html",
                        file_for_week_day=for_week_days_shift,
                        file_for_weekend=for_staff_weekend_shift

                                        )

         return page_content

     if __name__ == "__main__":
         app.run (debug=True)

