from flask import ( 
    Blueprint,
    render_template,
    request,
    session,
    g,
    redirect,
    url_for,
    make_response
)

from dbhelper import dbhelper

db = dbhelper()

login_bp = Blueprint('login_bp', __name__)

@login_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = db.authenticateUser(email, password)
        if user:
            session["username"] = email
            g.user = user
            return redirect(url_for("dashboard_bp.dashboard"))
        else:
            message = {
                'icon': '',
                'title': 'Account not found',
                'body': 'Username/Password incorrect',
                'action1': 'OK',
                'action1url': url_for("login_bp.login")
            }
            return render_template("login.html", message=message)

    return render_template("login.html")

@login_bp.route('/logout')
def logout():
    g.user = None
    session.pop('username', None)

    response = make_response(redirect(url_for('login_bp.login')))

    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    redirect_url = url_for('login_bp.login')
    response.headers['Location'] = redirect_url

    return response