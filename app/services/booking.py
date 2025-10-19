# app/services/parser.py

from flask import request, Blueprint, render_template
from flask_login import login_required, current_user
from ..models import Student, Teacher, Course, Time, Classes, Slot, User
from app import db
from ..models import Classes, Time,User
from sqlalchemy.orm import aliased
from sqlalchemy import and_
from datetime import date

bp=Blueprint('booking', __name__)


#__________________________________________________________________________________
# gives the week's schedule of the selected teacher
def get_todays_schedule(user_id):


    time_alias = aliased(Time)

    # queries the db using the system date, probably change to a more accurate system later

    # this query function could also be used to get the teacher schedule
    query_result = (
        db.session.query(
            Classes.day,                  # <-- include day here
            time_alias.start,
            time_alias.end,
            Classes.course_id
        )
        .select_from(User)
        .join(Classes, User.id == Classes.user_id)
        .join(time_alias, and_(
            time_alias.column_id == Classes.column_id,
            time_alias.course_type == Classes.course_type
        ))
        .filter(
            User.id == int(user_id),
        )
        .all()
    )


    formatted_sessions = [
        {"day": day, "start": start, "end": end, "course_code": code}
        for day, start, end, code in query_result
    ]
    
    return formatted_sessions
#____________________________________________________
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

#__________________________________________________________________________________
        all_slots=[
            {"start":'08:00', "end":'08:50'},
            {"start":'08:00', "end":'08:50'},
            {"start":'09:00', "end":'09:50'},
            {"start":'08:51', "end":'09:40'},
            {"start":'10:00', "end":'10:50'},
            {"start":'09:51', "end":'10:40'},
            {"start":'11:00', "end":'11:50'},
            {"start":'10:41', "end":'11:30'},
            {"start":'12:00', "end":'12:50'},
            {"start":'11:40', "end":'12:30'},
            {"start":'14:00', "end":'14:50'},
            {"start":'12:31', "end":'13:20'},
            {"start":'15:00', "end":'15:50'},
            {"start":'14:00', "end":'14:50'},
            {"start":'16:00', "end":'16:50'},
            {"start":'14:51', "end":'15:40'},
            {"start":'17:00', "end":'17:50'},
            {"start":'15:51', "end":'16:40'},
            {"start":'18:00', "end":'18:50'},
            {"start":'16:41', "end":'17:30'},
            {"start":'18:51', "end":"19:00"},
            {"start":'17:40', "end":'18:30'},
            {"start":'19:01', "end":'19:50'},
            {"start":'18:31', "end":'19:20'},
        ]

        all_days=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

        booked_dict = { (slot['day'], slot['start'], slot['end']): slot['course_code'] for slot in teacher_schedule }

        timetable_grid = []
        for day in all_days:
            row = []
            for slot in all_slots:
                course = booked_dict.get((day, slot['start'], slot['end']), "")
                row.append({
                    'start': slot['start'],
                    'end': slot['end'],
                    'course_code': course,
                    'day': day
                })

            timetable_grid.append({'day': day, 'slots': row})
        return render_template('booking.html', timetable=timetable_grid, all_slots=all_slots)
                
    return render_template('booking.html')


    