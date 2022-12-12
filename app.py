import calendar
from datetime import datetime
from flask import Flask, render_template
import mymodule

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    date_time = datetime.now()
    calendar_year = calendar.TextCalendar()
    page_content = render_template("home.html",
                                   current_time=date_time,
                                   calendar_year=calendar_year.formatyear(2023, w=2, l=1, c=6, m=3)
                                   )
    return page_content


@app.route('/staff')
def staff():
    for_week_days_shift = mymodule.open_staff_file("staff_week_day.txt", ":")
    for_staff_weekend_shift = mymodule.open_staff_file("staff_weekend.txt", "=")
    page_content = render_template("staff.html",
                                   for_week_days_shift=for_week_days_shift,
                                   for_staff_weekend_shift=for_staff_weekend_shift
                                   )
    return page_content


if __name__ == "__main__":
    app.run(debug=True)
