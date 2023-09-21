import os
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template
)
import traceback


from routes.register import register_bp
from routes.login import login_bp
from routes.dashboard import dashboard_bp
from routes.settings import settings_bp
from routes.favourites import favourites_bp

from dbhelper import dbhelper

load_dotenv()
db = dbhelper()

#db.setup()

app = Flask(__name__)

app.register_blueprint(login_bp)    
app.register_blueprint(register_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(settings_bp)
app.register_blueprint(favourites_bp)

app.secret_key = os.getenv('SECRET_KEY')

@app.errorhandler(Exception)
def handle_exception(error):
    error_message = str(error)
    traceback_info = traceback.format_exc()

    print(traceback_info)
    return render_template('error.html')

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5200")),
        debug=os.getenv('DEBUG')
    )