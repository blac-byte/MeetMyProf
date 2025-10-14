# app/models/time.py

from .. import db


class Time(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    #user_id needs to be later removed to make this table universal
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))  
    column_id=db.Column(db.Integer)
    start=db.Column(db.String(20), nullable=False)
    end=db.Column(db.String(20), nullable=False)
    course_type=db.Column(db.String(10))

    student = db.relationship('User', backref='time')

    def __init__(self, user_id, column_id, start, end, course_type):
        self.user_id=user_id
        self.column_id=column_id
        self.start=start
        self.end=end
        self.course_type=course_type

