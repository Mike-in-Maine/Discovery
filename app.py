from flask import Flask, redirect, url_for, render_template, url_for

from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
class todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    completed = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default = datetime)
    def __repr__(self):
        return'<Task %r>' % self.id
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/adminadmin")
def admin():
    return redirect(url_for("/"))


if __name__ == "__main__":
    app.run(debug=True)