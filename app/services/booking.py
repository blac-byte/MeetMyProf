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
        department=department if department else None

        teacher_id=db.session.query(Teacher.user_id).filter_by(name=teacher_name, department=department).first()
        teacher_id=int(teacher_id[0]) if teacher_id else None

        teacher_schedule=get_todays_schedule(teacher_id)
        print('Bookings')
        print(teacher_schedule)


    return render_template('booking.html')


    