import json

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from blog_flask_app.database import db

app = Flask(__name__)
Bootstrap5(app)

with open("data/holiday_journal.json") as f:
    holiday_journals = json.load(f)

with open("data/data_blog_posts.json") as f:
    data_blogs = json.load(f)

# CREATE DATABASE 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
with app.app_context():
    db.init_app(app)
    db.create_all()


@app.route('/')
def get_all_posts():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/journals')
def get_holiday_journals():
    return render_template("journals.html", journals=holiday_journals)

@app.route('/data_blogs')
def get_data_blogs():
    return render_template("data_blogs.html", blog_posts=data_blogs)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
