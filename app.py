import datetime

from flask import Flask, render_template

app = Flask (__name__)

@app.route ('/')
@app.route ('/home')
def home():
    today = datetime.date.today( )
    from_file = readfile("master.txt")
    return render_template ("home.html")


@app.route ('/staff')
def staff():
    today = datetime.date.today( )
    return render_template ("staff.html")

@app.route
def user(name, id):
    return "User page:" + name + str (id)


if __name__ == "__main__":
    app.run (debug=True)
