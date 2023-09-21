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
@login_required
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
    message = session.pop('message', None)

    return render_template("settings.html", user=user, selecteditem=selecteditem, message=message)
    
@settings_bp.route("/deleteaccount", methods=["POST"])
@login_required
def deleteaccount():
    email = session.get('username')
    db.deleteuser(email)
    session.clear()
    return redirect('/')

