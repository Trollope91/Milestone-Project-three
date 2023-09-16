from flask import ( 
    Blueprint,
    render_template,
    request,
    session,
    g,
    redirect,
    url_for
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
    return render_template("login.html")