# app/models/booking.py

from .. import db
from datetime import datetime

class Booking(db.Model):
    __tablename__ = 'booking'

    id = db.Column(db.Integer, primary_key=True)
    
    student_id = db.Column(db.Integer, db.ForeignKey('student.user_id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.s_no'), nullable=False)

    day = db.Column(db.String(10), nullable=False)
    start = db.Column(db.String(20), nullable=False)
    end = db.Column(db.String(20), nullable=False)


    status = db.Column(db.String(20), default='confirmed')

    # Relationships
    student = db.relationship('Student', backref='bookings')
    teacher = db.relationship('Teacher', backref='bookings')


    def __init__(self, student_id, teacher_id, day, start, end, status):
        self.student_id = student_id
        self.teacher_id = teacher_id
        self.day = day
        self.start = start
        self.end = end
        self.status = status
        