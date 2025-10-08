# app/models/teacher_info.py

from .. import db
from flask_login import UserMixin



class Teacher(db.Model, UserMixin):
    s_no = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), unique=False)
    department = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    user=db.relationship('User', back_populates='teacher')

    @property
    def role(self):
        return "teacher"
    
    def get_id(self):
        return str(self.user_id)
    

