# app/models/booking.py

from .. import db
from datetime import datetime

class Booking(db.Model):
    __tablename__ = 'booking'

    id = db.Column(db.Integer, primary_key=True)
    
    student_id = db.Column(db.Integer, db.ForeignKey('student.user_id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.s_no'), nullable=False)

    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    student = db.relationship('Student', backref='bookings')
    teacher = db.relationship('Teacher', backref='bookings')


