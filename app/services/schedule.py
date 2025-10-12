# app/services/schedule.py

from app import db
from flask_login import current_user
from ..models import Student, Classes, Time
from sqlalchemy.orm import aliased
from sqlalchemy import and_
from datetime import date


def get_todays_schedule():
    user_id=current_user.get_id()
    today = date.today()
    abbreviated_day_name = today.strftime("%a").upper()


    time_alias = aliased(Time)

    # queries the db using the system date, probably change to a more accurate system later
    results = (
        db.session.query(time_alias.start, time_alias.end, Classes.course_id)
        .select_from(Student)
        .join(Classes, Student.reg_id == Classes.reg_id)
        .join(time_alias, and_(
            time_alias.column_id == Classes.column_id,
            time_alias.course_type == Classes.course_type
        ))
        .filter(    
            Student.reg_id == int(user_id),
            Classes.day == abbreviated_day_name
        )
        .all()
    )


    return results, abbreviated_day_name
