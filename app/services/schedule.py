# app/services/schedule.py

from app import db
from ..models import Classes, Time,User
from sqlalchemy.orm import aliased
from sqlalchemy import and_
from collections import defaultdict

def get_todays_schedule(user_id):
    
    time_alias = aliased(Time)

    # queries the db for the entire week!

    # this query function is used for both dashboard and booking pages
    query_result = (
        db.session.query(Classes.day, time_alias.start, time_alias.end, Classes.course_id)
        .select_from(User)
        .join(Classes, User.id == Classes.user_id)
        .join(time_alias, and_(
            time_alias.column_id == Classes.column_id,
            time_alias.course_type == Classes.course_type
        ))
        .filter(    
            User.id == int(user_id)
        )
        .all()
    )


    grouped_schedule = defaultdict(list)
    for day, start, end, course_code in query_result:
        grouped_schedule[day].append({
            'day': day,
            'start': start,
            'end': end,
            'course_code': course_code
        })
    

    grouped_schedule=dict(grouped_schedule)
    # the code below since schedule.py doesn't have any keys : 'SAT' , 'SUN'
    # and since those are blank in the actual timetable we just give placeholder values
    grouped_schedule['SAT'],grouped_schedule['SUN']=[],[]

    return grouped_schedule 
