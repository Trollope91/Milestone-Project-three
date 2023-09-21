from decorators.login_required import login_required
from dbhelper import dbhelper
from flask import (
    Blueprint,
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()

db = dbhelper()

favourites_bp = Blueprint('favourites_bp', __name__)

@favourites_bp.route("/favourites", methods=["GET", "POST"])
@login_required
def favourites():
    """
    Render the user's favorites page.

    """
    logged_in_user = db.getuserbyusername(session.get('username'))
    
    if not all(logged_in_user.get(key) for key in ['firstname', 'lastname', 'profile_picture', 'dob']):
        message = {
            'icon': 'Please provide an image, firstname, lastname and dob',
            'title': 'Please fill in your profile settings',
            'body': 'This will give users access to your profile also',
            'action1': 'OK',
            'action1url': url_for("settings_bp.settings")
        }
        session['message'] = message

        return redirect(url_for('settings_bp.settings'))

    selecteditem = "favourites"
    userList = db.get_favourite_users(logged_in_user)
    return render_template("favourites.html", user=logged_in_user, selecteditem=selecteditem, userList=userList)


@favourites_bp.route("/removeuserfromfavourite", methods=["GET", "POST"])
@login_required
def removeuserfromfavourite():
    """
    Remove a user from the current user's list of favorites.

    """
    user = db.getuserbyusername(session.get('username'))
    favouriteuser = int(request.form.get("displayeduserid"))
    db.removeuserfromfavourite(user, favouriteuser)
    return redirect('/favourites')


@favourites_bp.route("/searchfavourites", methods=["GET", "POST"])
@login_required
def searchfavourites():
    """
    Search for favorite users by a particular field.

    """
    logged_in_user = db.getuserbyusername(session.get('username'))
    searchField = request.form.get("search_field")

    if not all(logged_in_user.get(key) for key in ['firstname', 'lastname', 'profile_picture', 'dob']):
        message = {
            'icon': 'Please provide an image, firstname, lastname and dob',
            'title': 'Please fill in your profile settings',
            'body': 'This will give users access to your profile also',
            'action1': 'OK',
            'action1url': url_for("settings_bp.settings")
        }
        session['message'] = message

        return redirect(url_for('settings_bp.settings'))

    selecteditem = "favourites"
    userList = db.get_favourite_users(logged_in_user, searchField)
    return render_template("favourites.html", user=logged_in_user, selecteditem=selecteditem, userList=userList)
