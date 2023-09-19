from flask import ( 
    Blueprint,
    render_template,
    session,
    request,
    redirect              
)

from base64helper import compressimagefrombase64

from dbhelper import dbhelper

from decorators.login_required import login_required

db = dbhelper()

settings_bp = Blueprint('settings_bp', __name__)

@settings_bp.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        email = request.form.get("email")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        bio = request.form.get("bio")
        dob = request.form.get("dob")
        picture = request.form['base64_image']
        compressed_picture = compressimagefrombase64(picture)
        
        db.updateuser(firstname, lastname, email, compressed_picture, bio, dob)
    user = db.getuserbyusername(session.get('username'))
    selecteditem = "settings"
    return render_template("settings.html", user=user, selecteditem=selecteditem)

@settings_bp.route("/deleteaccount", methods=["POST"])
def deleteaccount():
    email = session.get('username')
    db.deleteuser(email)
    session.clear()
    return redirect('/')

