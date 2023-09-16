import os
from dotenv import load_dotenv
from flask import Flask

from routes.register import register_bp
from routes.login import login_bp
from routes.dashboard import dashboard_bp
from routes.settings import settings_bp

from dbhelper import dbhelper

load_dotenv()
db = dbhelper()

app = Flask(__name__)

app.register_blueprint(login_bp)    
app.register_blueprint(register_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(settings_bp)

app.secret_key = os.getenv('SECRET_KEY')

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5200")),
        debug=True)