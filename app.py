import os
import bcrypt
from flask import Flask, render_template, url_for, request, redirect, \
     flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists('env.py'):
    import env

app = Flask(__name__)

# Environment Variables
app.config["MONGO_DBNAME"] = 'rehearsal_room'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/the_band_room')
# Default landing page
def the_band_room():
    return render_template('addbandroom.html')


@app.route('/register_user', methods=['POST', 'GET'])
def register_user():
    if request.method == 'POST':
        users = mongo.db.users
        already_user = users.find_one({'user_name': request.form['user_name']})

        if already_user is None:
            hashpass = bcrypt.hashpw(request.form['user_key'].encode('utf-8'),
                                     bcrypt.gensalt())
            users.insert_one({'user_name': request.form['user_name'],
                              'user_key': hashpass})
            session['user_name'] = request.form['user_name']
            return redirect(url_for('the_band_room'))

        return 'That username already exists!'

    return render_template('register.html')


# This function adds a new band room
@app.route('/add_room', methods=['POST'])
def add_band_room():
    room_key = request.form["room_key"]
    """
    iterate over stored band rooms to check
    if the room key is available
    """
    check_key = mongo.db.band_rooms.count_documents((
        {"room_key": room_key}))
    if check_key > 0:
        flash('Sorry that username and room key is unavailable', 'error')
        return redirect(url_for('the_band_room'))
    # if the key is available the room will be created
    else:
        new_room = mongo.db.band_rooms
        new_room.insert_one(request.form.to_dict())
        flash('Room created successfully', 'success')
        return redirect(url_for('browse_rooms'))


# This function displays all the rooms to the user
@app.route('/browse_rooms')
def browse_rooms():
    return render_template('browserooms.html',
                           band_rooms=mongo.db.band_rooms.find())


# This function finds the selected room and displays the room to the user
@app.route('/my_room/<room_id>')
def my_room(room_id):
    the_room = mongo.db.band_rooms.find_one({'_id': ObjectId(room_id)})
    return render_template('bandroom.html', room=the_room)


@app.route('/edit_room/<room_id>')
def edit_room(room_id):
    the_room = mongo.db.band_rooms.find_one({'_id': ObjectId(room_id)})
    return render_template('editroom.html', room=the_room)


@app.route('/update_room/<room_id>', methods=['POST'])
def update_room(room_id):
    rooms = mongo.db.band_rooms
    rooms.update({'_id': ObjectId(room_id)},
                 {'$set':
                  {'band_name': request.form.get('band_name'),
                   'band_notes': request.form.get('band_notes'),
                   'social_media': request.form.get('social_media')
                   }})
    return redirect(url_for('browse_rooms'))


@app.route('/delete_room/<room_id>')
def delete_room(room_id):
    mongo.db.band_rooms.remove({'_id': ObjectId(room_id)})
    return redirect(url_for('browse_rooms'))


if __name__ == '__main__':
    app.secret_key = 'super secret key'

    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
