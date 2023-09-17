from flask import ( 
    Blueprint,
    render_template             
)

favourites_bp = Blueprint('favourites_bp', __name__)

@favourites_bp.route("/favourites", methods=["GET", "POST"])
def favourites():
    return render_template("favourites.html", selecteditem="favourites")
