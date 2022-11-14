from datetime import datetime

from flask import Flask, render_template

app = Flask (__name__)



@app.route ('/')
@app.route ('/home')
def home():
    today = datetime.now( )
    page_content = render_template(
        "home.html",
        curent_year = today.year
    )

    return page_content 

@app.route ('/staff')
def staff():
    today = datetime.now( )
    calendar_itiem = "123"
    return render_template (
        "staff.html",
        curent_year = today.year,
        calendar_itiem = calendar_itiem

    )

@app.route
def user(name, id):
    return "User page:" + name + str (id)


if __name__ == "__main__":
    app.run (debug=True)
