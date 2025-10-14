# routes/dashboard.py

from flask import render_template, Blueprint, session, request
from flask_login import login_required
from app.services.schedule import get_todays_schedule

bp=Blueprint('dashboard', __name__)

@bp.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
    schedule=session.get('schedule')
    abbreviated_day_name = session.get("abbreviated_day_name")
    
    if not schedule or not abbreviated_day_name:
        get_todays_schedule()
        return render_template('dashboard.html', schedule = session.get('schedule',[]), abbreviated_day_name = session.get("abbreviated_day_name"))
    
    return render_template('dashboard.html', schedule = session.get('schedule',[]), abbreviated_day_name = abbreviated_day_name)