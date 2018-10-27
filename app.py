from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_surfing


app = Flask(__name__)


#mongo = PyMongo(app, uri="mongodb://localhost:27017/surfing_app")


@app.route('/')
def index():
    #surfing = mongo.db.surfing.find_one()
    return render_template('index.html')


@app.route('/wordanalysis')
def wa():
    return render_template('wordanalysis.html')

@app.route('/funfacts')
def ff():
    return render_template('funfacts.html')
if __name__ == "__main__":
    app.run(debug=True)
