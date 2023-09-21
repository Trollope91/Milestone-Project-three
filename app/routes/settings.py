from flask import ( 
    Blueprint,
    render_template,
    session,
    request,
    redirect,
    url_for        
)

from werkzeug.security import generate_password_hash

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

@settings_bp.route('/updatepassword', methods=["POST"])
@login_required
def updatepassword():
    user = db.getuserbyusername(session.get('username'))
    current_password = request.form.get("current_password")
    new_password = request.form.get("new_password")
    confirm_password = request.form.get("confirm_password")
    #check current password is correct
    user = db.authenticateUser(user['email'], current_password)
    if user:
        #does the new password match the current password
        if new_password != confirm_password:
            message = {
                'icon': '',
                'title': 'Passwords do not match, please try again',
                'body': '',
                'action1': 'OK',
                'action1url': url_for("settings_bp.settings")
            }
            session['message'] = message

            return redirect(url_for('settings_bp.settings'))
        else:
            hashed_password = generate_password_hash(new_password, method='sha256')
            db.updatepasswordforuser(user,hashed_password)
            message = {
                'icon': '',
                'title': 'Successfully updated password',
                'body': '',
                'action1': 'OK',
                'action1url': url_for("settings_bp.settings")
            }
            session['message'] = message

            return redirect(url_for('settings_bp.settings'))
            
    else:
        message = {
            'icon': '',
            'title': 'Current password is incorrect',
            'body': '',
            'action1': 'OK',
            'action1url': url_for("settings_bp.settings")
        }
        session['message'] = message

        return redirect(url_for('settings_bp.settings'))
