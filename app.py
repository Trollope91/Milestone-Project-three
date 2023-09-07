import os
from flask import Flask

from routes.register import register_bp
from routes.login import login_bp
from routes.dashboard import dashboard_bp


app = Flask(__name__)

app.register_blueprint(login_bp)    
app.register_blueprint(register_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)