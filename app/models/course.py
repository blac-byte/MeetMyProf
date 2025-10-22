# app/models/course.py

from .. import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_id = db.Column(db.String(20), nullable=False)
    course_type = db.Column(db.String(3), unique=False)
    batch = db.Column(db.String(10), unique=False)

   
    def __init__(self, course_id, course_type, batch):
        self.course_id = course_id
        self.course_type = course_type
        self.batch = batch
        

    @staticmethod
    def insert_sample_course():
        """Insert default course rows if table is empty."""
        if Course.query.first():
            return  # Skip if data already exists
        course = [
            Course(course_id="BAEEE101", course_type="ETH", batch='ALL03'),
            Course(course_id="BAEEE101", course_type="ELA", batch='ALL03'),

            Course(course_id="BACSE103", course_type="ELA", batch='ALL03'),
            Course(course_id="BACSE103", course_type="ETH", batch='ALL03'),

            Course(course_id="BAMAT101", course_type="ETH", batch='ALL03'),
            Course(course_id="BAMAT101", course_type="ELA", batch='ALL03'),

            Course(course_id="BACHY105", course_type="ETH", batch='ALL03'),
            Course(course_id="BACHY105", course_type="ELA", batch='ALL03'),
            
            Course(course_id="BACSE101", course_type="LO", batch='ALL03'),
            
            
            
        ]

        for i in course:
            db.session.add(i)
        db.session.commit()
