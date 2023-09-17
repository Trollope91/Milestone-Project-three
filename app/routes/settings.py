from flask import ( 
    Blueprint,
    render_template,
    session              
)

from dbhelper import dbhelper

db = dbhelper()

settings_bp = Blueprint('settings_bp', __name__)

@settings_bp.route("/settings", methods=["GET", "POST"])
def settings():
    user = db.getuserbyusername(session.get('username'))
    return render_template("settings.html", user=user, selecteditem="settings")