from flask import (
    Blueprint,
    render_template,
    session,
    make_response
)

import random

import datetime

from dbhelper import dbhelper

db = dbhelper()

dashboard_bp = Blueprint('dashboard_bp', __name__)


@dashboard_bp.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    user = db.getuserbyusername(session.get('username'))
    user = db.getAllUsers()
    user = random.choice(user)
    try:
        # Attempt to parse DOB as 'YYYY-MM-DD'
        age = getagefromdob(user['dob'])
    except ValueError:
        age = "unknown"

    user['age'] = age
    session["displayeduserid"] = user["id"]
    response = make_response(render_template(
        "dashboard.html", selecteditem="dashboard", user=user))

    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response

def getagefromdob(dob):
    if not dob:
        return "unknown"
    try:
        # Attempt to parse DOB as 'YYYY-MM-DD'
        dob_date = datetime.datetime.strptime(dob, '%Y-%m-%d')
    except ValueError:
        try:
            # If parsing as 'YYYY-MM-DD' fails, try 'DD-MM-YYYY'
            dob_date = datetime.datetime.strptime(dob, '%d-%m-%Y')
        except ValueError:
            return "Unknown"
    today = datetime.date.today()
    age = today.year - dob_date.year - \
        ((today.month, today.day) < (dob_date.month, dob_date.day))
    return age
