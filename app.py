import os
from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


# Environment Variables
app.config["MONGO_DBNAME"] = "rehearsal_room"
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/the_band_room')
def the_band_room():
    return render_template("addbandroom.html")


@app.route('/band_room')
def get_band_rooms():
    return render_template("bandroom.html",
                           band_rooms=mongo.db.band_rooms.find(),
                           events=mongo.db.events.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
