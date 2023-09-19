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
def favourites():
    user = db.getuserbyusername(session.get('username'))
    selecteditem = "favourites"
    userList = db.get_favourite_users(user)
    return render_template("favourites.html", user=user, selecteditem=selecteditem, userList=userList)


@favourites_bp.route("/removeuserfromfavourite", methods=["GET", "POST"])
def removeuserfromfavourite():
    user = db.getuserbyusername(session.get('username'))
    favouriteuser = int(request.form.get("displayeduserid"))
    db.removeuserfromfavourite(user,favouriteuser)
    return redirect ('/favourites')