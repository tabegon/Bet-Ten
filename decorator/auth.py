from functools import wraps

from flask import flash, redirect, session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Veuillez vous connecter pour acceder à cette page', 'warning')
            return redirect('/logout')
        return f(*args, **kwargs)
    return decorated_function