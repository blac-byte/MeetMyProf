# app/models/student.py

from .. import db
from sqlalchemy import Enum
from flask_login import UserMixin



class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    batch=db.Column(db.String(10), unique=False, nullable=True)
    email=db.Column(db.String(100), unique=True, nullable=False)
    user=db.relationship('User', back_populates='student')


    @property
    def role(self):
        return "student"

    def get_id(self):
        return str(self.user_id)

  


