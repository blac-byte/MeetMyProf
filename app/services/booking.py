# app/services/parser.py

from flask import request, Blueprint, url_for, redirect, render_template
from flask_login import login_required, current_user
from ..models import Student, Teacher, Course, Time, Classes, Slot
from app import db
from sqlalchemy.orm import aliased
from sqlalchemy import and_


bp=Blueprint('booking', __name__)

@bp.route('/booking', methods=['GET','POST'])
@login_required
def booking():





    for slot, course_id, user_id in result:
        print(slot.slot_id, course_id, user_id)



    return render_template('booking.html')


    