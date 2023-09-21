from functools import wraps
from flask import request, redirect, url_for, session

def login_required(func):
    """
    A decorator for protecting routes that require user authentication.

    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login_bp.login'))
    
    return wrapper

