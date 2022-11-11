from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("main.html")


@app.route('/staff')
def staff():
    return render_template("staff.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page:" + name + str(id)


if __name__ == "__main__":
    app.run(debug=True)
