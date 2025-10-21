# app/models/time.py

from .. import db

class Time(db.Model):
    __tablename__ = 'time'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    column_id = db.Column(db.Integer)
    start = db.Column(db.String(20), nullable=False)
    end = db.Column(db.String(20), nullable=False)
    course_type = db.Column(db.String(10))

    def __init__(self, column_id, start, end, course_type):
        self.column_id = column_id
        self.start = start
        self.end = end
        self.course_type = course_type

    @staticmethod
    def insert_default_time():
        """Insert default time rows if table is empty."""
        if Time.query.first():
            return  # Skip if data already exists

        time = [
            Time(0, '08:00', '08:50', 'ETH'),
            Time(0, '08:00', '08:50', 'ELA'),
            Time(1, '09:00', '09:50', 'ETH'),
            Time(1, '08:51', '09:40', 'ELA'),
            Time(2, '10:00', '10:50', 'ETH'),
            Time(2, '09:51', '10:40', 'ELA'),
            Time(3, '11:00', '11:50', 'ETH'),
            Time(3, '10:41', '11:30', 'ELA'),
            Time(4, '12:00', '12:50', 'ETH'),
            Time(4, '11:40', '12:30', 'ELA'),
            Time(5, '14:00', '14:50', 'ETH'),
            Time(5, '12:31', '13:20', 'ELA'),
            Time(6, '15:00', '15:50', 'ETH'),
            Time(6, '14:00', '14:50', 'ELA'),
            Time(7, '16:00', '16:50', 'ETH'),
            Time(7, '14:51', '15:40', 'ELA'),
            Time(8, '17:00', '17:50', 'ETH'),
            Time(8, '15:51', '16:40', 'ELA'),
            Time(9, '18:00', '18:50', 'ETH'),
            Time(9, '16:41', '17:30', 'ELA'),
            Time(10, '18:51', '19:00', 'ETH'),
            Time(10, '17:40', '18:30', 'ELA'),
            Time(11, '19:01', '19:50', 'ETH'),
            Time(11, '18:31', '19:20', 'ELA'),
        ]

        for i in time:
            db.session.add(i)
        db.session.commit()
