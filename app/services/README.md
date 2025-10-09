## Services
Services folder is the core of this web app. This controls all the services provided by the webapp 
- Timetable parsing
- Schedule querying
- Appointment booking

The folder has different files
1. parser.py
   parser.py is the file that parses through the copy pasted timetable in the textarea.
1. schedule.py
   schedule.py does the query for the present day's schedule.
   ```python
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
   ```
