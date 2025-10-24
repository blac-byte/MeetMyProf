# app/services/schedule.py

from app import db
from ..models import Classes, Time,User
from sqlalchemy.orm import aliased
from sqlalchemy import and_
from collections import defaultdict

# this function is used for both dashboard and booking pages
def get_todays_schedule(user_id):
    
    time_alias = aliased(Time)

    # queries the db for the entire week!

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

    # the code is due to no entries for 'SAT' and 'SUN'
    # but since the table is fed with this data they are added as
    # placeholders
    grouped_schedule['SAT'],grouped_schedule['SUN']=[],[]

    return grouped_schedule 
