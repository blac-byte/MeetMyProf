# app/services/schedule.py

from app import db
from ..models import Classes, Time,User
from sqlalchemy.orm import aliased
from sqlalchemy import and_
from datetime import date
from flask import session

def get_todays_schedule(user_id):
    today = date.today()
    abbreviated_day_name = today.strftime("%a").upper()


    time_alias = aliased(Time)

    # queries the db using the system date, probably change to a more accurate system later

    # this query function could also be used to get the teacher schedule
    query_result = (
        db.session.query(time_alias.start, time_alias.end, Classes.course_id)
        .select_from(User)
        .join(Classes, User.id == Classes.user_id)
        .join(time_alias, and_(
            time_alias.column_id == Classes.column_id,
            time_alias.course_type == Classes.course_type
        ))
        .filter(    
            User.id == int(user_id),
            Classes.day == abbreviated_day_name
        )
        .all()
    )


    formatted_sessions = [
        {"day": abbreviated_day_name, "start": start, "end": end, "course_code": code}
        for start, end, code in query_result
    ]


    session["schedule"] = formatted_sessions
    session["abbreviated_day_name"] = abbreviated_day_name
    
    return formatted_sessions
