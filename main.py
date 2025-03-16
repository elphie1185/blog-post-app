from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)

journals = [
    {
        "title": "Paris 2021",
        "trip_description": "A trip to Paris",
        "date": "2021-01-01",
        "entries": [
            {
                "date": "2020-12-01",
                "entry_text": "I went to Paris and it was amazing!"
            }, 
            {
                "date": "2020-12-02",
                "entry_text": "I went to the Eiffel Tower"
            },
            {
                "date": "2020-12-03",
                "entry_text": "I went to the Louvre"
            }
        ]
    }
]

@app.route('/')
def get_all_posts():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/journals')
def get_holiday_journals():
    return render_template("journals.html", journals=journals)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
