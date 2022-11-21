import calendar
from datetime import datetime
from flask import Flask, render_template

app = Flask (__name__)

@app.route ('/')
@app.route ('/home')
def home():
    today = datetime.now( )
    c = calendar.TextCalendar()
    page_content = render_template("home.html",
     current_year = today.year,
     calendar_year = c.formatyear(2002, w=2, l=1, c=6, m=3)

    )
    return page_content


@app.route ('/staff')
def staff():
    
    today = datetime.now( )
    c = calendar.TextCalendar()
    file = open ("master.txt", 'r')
    time_table = {}
    for line in file:
        (key, val) = line.split (':')
        time_table[key] = val


    page_content =  render_template(
        "staff.html",
         current_year = today.year,
         calendar_year =c.formatyear(2002, w=2, l=1, c=6, m=3),
         staff_fale = time_table
    )


    return page_content


if __name__ == "__main__":
    app.run (debug=True)
