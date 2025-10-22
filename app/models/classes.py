# app/models/classes.py

from .. import db


class Classes(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))                 
    course_id=db.Column(db.String(20), nullable=False)
    course_type=db.Column(db.String(10))
    day=db.Column(db.String(3))

    building = db.Column(db.String(10), unique=False, nullable=True)
    room = db.Column(db.String(10), unique=False, nullable=True)
    column_id=db.Column(db.Integer)
    slot_id=db.Column(db.String(3))

    user = db.relationship('User', backref='classes')

    # used to prevent duplicate slot entry for the user
    __table_args__ = (
        db.UniqueConstraint('user_id', 'slot_id', 'day', name='uq_user_slot'),
    )

    def __init__(self, user_id, course_id, course_type, day, building, room, column_id, slot_id):
        self.user_id=user_id
        self.course_id=course_id
        self.course_type=course_type
        self.day=day
        self.building=building
        self.room=room
        self.column_id=column_id
        self.slot_id=slot_id