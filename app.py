import app
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, reguest, redirect

import mymodule

app = Flask(__name__)
app.config['SQLALCHEMY DATABASE_URI'] = 'sqllite:///staff_shift.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Colum(db.Integer, primary_key=True)
    title = db.Colum(db.Integer(100), primary_key=True)
    intro = db.Colum(db.Integer(300), primary_key=True)
    text = db.Colum(db.Integer, primary_key=True)
    date = db.Colum(db.DateTime, default=datetime.utcnow)
    
    
    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/crest-article', methhod=['POST', 'GET'])
def create_article():
    if reguest.method == "POST":
        pass
        title = reguest.form['title']
        intro = reguest.form['intro']
        text = reguest.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/home')
        except:
            return "For appload text return Error"
    else:
        return render_template("db_data.html")

@app.route('/')
@app.route('/home')
def home():
    date_time = datetime.now()
    page_content = render_template("home.html",
            current_time=date_time,
    )
    return page_content


@app.route('/staff')
def staff():
    for_week_days_shift = mymodule.work_with_db_json_staff_shift(
        "staff.json", 'weekday')
    for_staff_weekend_shift = mymodule.work_with_db_xml_staff_shift(
        "staff_weekend.xml", 'day', 'time')
    page_content = render_template(
        "staff.html",
        for_week_days_shift=for_week_days_shift,
        for_staff_weekend_shift=for_staff_weekend_shift
    )
    return page_content


if __name__ == "__main__":
    app.run(debug=True)
