from datetime import datetime
from flask import Flask, render_template, request, redirect
from sqlalchemy import MetaData, Table, Column, Integer, String, Text, ForeignKey
import mymodule





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///staff_shift.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
metadata = MetaData()
staff_name_surname = Table('staff_name_surname', metadata,
             Column('Name', String(200), primary_key=True),
             Column('Surname', String(200), nullable=False),

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    intro = db.Column(db.String(80), unique=True, nullable=False)
    text = db.Column(db.Text, unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Article %r>' % self.id



@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if  request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

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
