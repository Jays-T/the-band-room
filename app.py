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
# Default landing page
def the_band_room():
    return render_template("addbandroom.html",
                           )


# This function adds a new band room
@app.route('/add_room', methods=['POST'])
def add_band_room():
    # take the information from the create room form
    owner_name = request.form["owner_name"]
    room_key = request.form["room_key"]
    # error message
    owner_key_not_available = "This user name and room key is not "\
        "available. Please use a different event key."
    # iterate over stored band rooms to check
    # if the name and room key are available
    check_user = mongo.db.band_rooms.count_documents((
        {"owner_name": owner_name,
         "room_key": room_key}))
    if check_user > 0:
        # if name and room key are not available
        return render_template('roomkeyerror.html',
                               owner_key_not_available=owner_key_not_available,
                               owner_name=owner_name,
                               room_key=room_key)
    # if both name and key are available the room will be created
    else:
        new_room = mongo.db.band_rooms
        new_room.insert_one(request.form.to_dict())
        return redirect(url_for('browse_rooms'))


@app.route('/band_room')
def get_band_rooms():
    return render_template("bandroom.html",
                           band_rooms=mongo.db.band_rooms.find(),
                           events=mongo.db.events.find())


@app.route('/browse_rooms')
def browse_rooms():
    return render_template("browserooms.html",
                           band_rooms=mongo.db.band_rooms.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
