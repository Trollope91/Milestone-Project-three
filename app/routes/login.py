from flask import ( 
    Blueprint,
    render_template              
)

login_bp = Blueprint('login_bp', __name__)

@login_bp.route("/", methods=["GET", "POST"])
def login():
    return render_template("login.html")