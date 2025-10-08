# app/models/user.py

from .. import db
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash as hash, check_password_hash as check
from flask_login import UserMixin

class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # 'student' or 'teacher'
    is_active = db.Column(db.Boolean, default=True)

    # One-to-one relationships
    student = db.relationship('Student', back_populates='user', uselist=False)
    teacher = db.relationship('Teacher', back_populates='user', uselist=False)

    def set_password(self, password):
        self.password_hash = hash(password, method='pbkdf2:sha256')

    def check_password(self, password):
        return check(self.password_hash, password)

    def get_id(self):
        return self.id
