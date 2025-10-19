# app/services/parser.py

from flask import request, Blueprint, url_for, redirect, render_template
from flask_login import login_required, current_user
from ..models import Student, Teacher, Course, Time, Classes, Slot, User
from app import db
from ..services.schedule import get_todays_schedule


bp=Blueprint('booking', __name__)

@bp.route('/booking', methods=['GET','POST'])
@login_required
def booking():
    if request.method=='POST':
        teacher_name=request.form.get('teacher_name')
        department=request.form.get('department')

        teacher_id=db.session.query(User.id).filter_by(name=teacher_name, role='teacher').first()

        if teacher_id:
            teacher_id=teacher_id[0]
            teacher_schedule = get_todays_schedule(teacher_id)
        print(teacher_schedule)

    return render_template('booking.html')

    