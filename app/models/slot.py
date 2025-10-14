# app/models/slot.py

from .. import db
from sqlalchemy import Enum


class Slot(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    slot_id=db.Column(db.String(100))
    day=db.Column(db.String(3))