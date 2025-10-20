# app/services/booking.py

from flask import request, Blueprint, render_template, jsonify
from flask_login import login_required
from ..models import Teacher
from app import db
from .schedule import get_todays_schedule

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

        teacher_week_table=get_todays_schedule(teacher_id)

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

        booked_dict = {}
        for day, slots in teacher_week_table.items():
            for slot in slots:
                booked_dict[(slot['day'], slot['start'], slot['end'])] = slot['course_code']

        timetable_grid = []
        for day in all_days:
            row = []
            for slot in all_slots:
                course = booked_dict.get((day, slot['start'], slot['end']), "")
                print(1,course)
                                                    
                row.append({
                    'start': slot['start'],
                    'end': slot['end'],
                    'course_code': course,
                    'day': day
                })

            timetable_grid.append({'day': day, 'slots': row})
        return render_template('booking.html', timetable=timetable_grid, all_slots=all_slots)
                
    return render_template('booking.html')


#_____________________________________________________________
@bp.route('/book_slot', methods=['POST'])
@login_required
def book_slot():
    data = request.get_json()
    # extract day, start, end, and handle booking
    return jsonify({'success': True, 'course_code': 'MYCOURSE123'})
