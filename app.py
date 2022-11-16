import calendar
from datetime import datetime

from flask import Flask, render_template

app = Flask (__name__)



@app.route ('/')
@app.route ('/home')
def home():
    today = datetime.now( )
    c = calendar.TextCalendar(calendar.SUNDAY)
    page_content = render_template\
        ("home.html",
        current_year = today.year,
        calendar_year = c.prmonth(2022,1,0,0)
    )

    return page_content

@app.route ('/staff')
def staff():
    today = datetime.now( )
    c = calendar.TextCalendar( )
    page_content =  render_template \
        ("staff.html",
        current_year = today.year,
        calendar_year = c.formatyear(2002, w=2, l=1, c=6, m=3 )

    )

    return page_content

@app.route
def user(name, id):
    return "User page:" + name + str (id)


if __name__ == "__main__":
    app.run (debug=True)
