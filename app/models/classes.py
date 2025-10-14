# app/models/time.py

from .. import db
from sqlalchemy import Enum


class Classes(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))                 
    course_id=db.Column(db.String(20), nullable=False) #             for now, change in future
    course_type=db.Column(db.String(10))
    day=db.Column(db.String(3))
    column_id=db.Column(db.Integer)
    slot_id=db.Column(db.String(3))
    role=db.Column(Enum('student','teacher'))

    student = db.relationship('User', backref='classes')


    def __init__(self, user_id, course_id, course_type, day, column_id, slot_id, role):
        self.user_id=user_id
        self.course_id=course_id
        self.course_type=course_type
        self.day=day
        self.column_id=column_id
        self.slot_id=slot_id
        self.role=role