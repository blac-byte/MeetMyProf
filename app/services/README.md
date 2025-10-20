## Services
Services folder is the core of this project. This controls all the services provided by the webapp 
- Timetable parsing
- Schedule querying
- Appointment booking

The folder has different files
1. parser.py
   parser.py is the file that parses through the copy-pasted timetable in the textarea.
   
1. schedule.py
   It queries the entire weeks schedule.
   schedule.py does the query for the present day's schedule. Schedule.py is used in both dashboard.py and booking.py
   
   #### **`python`**
   ```python 
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
   ```
1. booking.py
   Queries the schedule of the selected teacher and formats them, then sends it to booking.html
