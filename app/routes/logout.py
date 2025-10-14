from flask import flash, redirect, url_for, Blueprint, session
from flask_login import login_required, logout_user

bp=Blueprint('logout', __name__)


@bp.route('/logout', methods=['GET','POST'])
@login_required
def logout():
        logout_user()#------------clears user data
        session.clear()#----------clears all session data
        return redirect(url_for('auth.signin'))#---------------add flash here