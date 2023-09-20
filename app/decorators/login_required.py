from functools import wraps
from flask import request, redirect, url_for, session

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' in session:
            # User is authenticated, so allow access to the dashboard
            return func(*args, **kwargs)
        else:
            # User is not authenticated, redirect to the login page
            return redirect(url_for('login_bp.login'))
    
    return wrapper
