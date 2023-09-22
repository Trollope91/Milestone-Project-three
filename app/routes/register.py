from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    session,
    g,
)
import re
from dbhelper import dbhelper
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

load_dotenv()

db = dbhelper()

register_bp = Blueprint('register_bp', __name__)

strong_password_pattern = (
    r"^(?=.*[A-Z])"  # At least one uppercase letter [A-Z]
    r"(?=.*[a-z])"   # At least one lowercase letter [a-z]
    r"(?=.*\d)"      # At least one digit [0-9]
    r"(?=.*[@#$%^&+=!])"  # At least one special character [@#$%^&+=!]
    r".{8,}$"         # Minimum length of 8 characters
)


@register_bp.route("/register", methods=["GET", "POST"])
def register():
    """
    Handle user registration.

    """
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("passwordConfirmation")

        if password != confirm_password:
            error = "Passwords do not match. Please try again."
            return render_template("register.html", error=error)

        if not re.match(strong_password_pattern, password):
            error = """Password is not strong enough.
            It should contain at least one uppercase letter,
            one lowercase letter, one digit, one special character,
            and be at least 8 characters long."""
            return render_template("register.html", error=error)

        hashed_password = generate_password_hash(password, method='sha256')

        if db.register(email, hashed_password):
            message = {
                'icon': 'success',
                'title': 'Successfully Registered',
                'body': 'You have successfully registered',
                'action1': 'Go to Dashboard',
                'action1url': url_for("dashboard_bp.dashboard"),
            }

            user = db.authenticateUser(email, password)
            session["username"] = email
            g.user = user
            return render_template("register.html", message=message)

        return render_template("login.html")

    return render_template("register.html")
