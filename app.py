from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
import json
from flask_heroku import Heroku

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku = Heroku(app)
db = SQLAlchemy(app)

class Dataentry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mydata = db.Column(db.Text())

@app.route("/submit", methods=["POST"])
def post_to_db():
    items = request.form['mydata']

    newitem = Dataentry(mydata=items)
    db.session.add(newitem)
    db.session.commit()

    return 'Success! To enter more data, <a href="{}">click here!</a>'.format(url_for("enter_data"))

@app.route("/")
def enter_data():
    return render_template("dataentry.html")

if __name__ == ' __main__':
    app.run(debug=True) 

