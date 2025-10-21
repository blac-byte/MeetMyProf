# app/routes/dashboard.py

from flask import render_template, Blueprint, session
from flask_login import login_required, current_user
from app.services.schedule import get_todays_schedule
from datetime import date

bp=Blueprint('dashboard', __name__)

@bp.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
    # rn dashboard.html is given the specific day as the arguement, later you can add a strip
    # with all the days of a week and incorporate it using javascript
    today=date.today()
    smol_day = today.strftime("%a").upper()
    week_table=session.get('timetable')

    user_id=current_user.get_id()
    session['timetable']=get_todays_schedule(user_id)
    print(session.get('timetable'))
    
    return ('hi')
    # if week_table:
    #     return render_template('dashboard.html', schedule = week_table[smol_day])
    
    # user_id=current_user.get_id()
    # session['timetable']=get_todays_schedule(user_id)
    # week_table=session.get('timetable')


    # return (render_template('dashboard.html', schedule = week_table[smol_day]))