from flask import (
    Blueprint,
    render_template,
    session,
    make_response,
    redirect,
    url_for
)

import random
import datetime
from dbhelper import dbhelper
from decorators.login_required import login_required

db = dbhelper()

dashboard_bp = Blueprint('dashboard_bp', __name__)


@dashboard_bp.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    """
    Render the user dashboard page.

    """
    logged_in_user = db.getuserbyusername(session.get('username'))

    # Check if required profile settings are missing
    if not all(logged_in_user.get(key) for key in ['firstname', 'lastname',
                                                   'profile_picture', 'dob']):
        message = {
            'icon': 'Please provide an image, firstname, lastname and dob',
            'title': 'Please fill in your profile settings',
            'body': 'This will give users access to your profile also',
            'action1': 'OK',
            'action1url': url_for("settings_bp.settings")
        }

        session['message'] = message
        return redirect(url_for('settings_bp.settings'))

    # Retrieve all users and select one at random
    user = db.getAllUsers()
    user = random.choice(user)

    try:
        age = getagefromdob(user['dob'])
    except ValueError:
        age = "unknown"

    user['age'] = age
    session["displayeduserid"] = user["id"]

    # Create a response with no caching
    response = make_response(render_template(
        "dashboard.html", selecteditem="dashboard", user=user))

    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response


def getagefromdob(dob):
    """
    Calculate the age based on the date of birth.

    """
    if not dob:
        return "unknown"
    try:
        dob_date = datetime.datetime.strptime(dob, '%Y-%m-%d')
    except ValueError:
        try:
            dob_date = datetime.datetime.strptime(dob, '%d-%m-%Y')
        except ValueError:
            return "Unknown"
    today = datetime.date.today()
    age = today.year - dob_date.year - \
        ((today.month, today.day) < (dob_date.month, dob_date.day))
    return age


@dashboard_bp.route("/addusertofavourite", methods=["GET", "POST"])
@login_required
def addusertofavourite():
    """
    Add a user to the current user's list of favorites.

    """
    user = db.getuserbyusername(session.get('username'))
    favouriteuser = session['displayeduserid']
    db.addusertofavourite(user, favouriteuser)
    return redirect('/dashboard')
