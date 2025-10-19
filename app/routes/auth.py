# app/routes/auth.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user
from app.utils.errors import is_student_email, is_teacher_email
from ..models import User, Student, Teacher
from .. import db



bp = Blueprint('auth', __name__)


#___________________________________________________________________________________________

@bp.route("/", methods=["GET", "POST"])
def signup():

    # If the user data is cached in the browser auto logs the user in
    if current_user.is_authenticated:
            return redirect(url_for('dashboard.dashboard')) 
    

##### Maybe add a token system where upon the click of the proceed button
##### an email is sent to the user to verify the user is the owner of the account







    
    # only triggers this if the proceed button is clicked
    if request.method=='POST':
        
        email=request.form.get('email').strip().lower()
        password=request.form.get('password')

        # checks for existing email, if not continues
        user=User.query.filter_by(email=email).first()
        if user:
            return 'already acc'

        # Here we are using function from app/utils/errors to check the password format
        # to verify the email is valid
        if is_student_email(email):
            role='student'
            user=User(email=email, role=role)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            student_entry=Student(user_id=user.id, email=email)
            db.session.add(student_entry)
            db.session.commit()

            login_user(user)
            return redirect(url_for('parser.parser'))
            
        # Here we are using function from app/utils/errors to check the password format
        # to verify the email is valid
        elif is_teacher_email(email):
            role='teacher'
            user=User(email=email, role=role)  
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            teacher_entry=Teacher(user_id=user.id, email=email)
            db.session.add(teacher_entry)
            db.session.commit()

            login_user(user)
            return redirect(url_for('parser.parser'))
            

        else:
            return 'Not a valid email'#---------------add flash here
    return render_template('auth/signup.html')


#__________________________________________________________________________________________

@bp.route('/signin',methods=['POST','GET'])          
def signin():

    # If the user data is cached in the browser auto logs the user in
    if current_user.is_authenticated:
            return redirect(url_for('dashboard.dashboard')) 
    

    if request.method=='POST':        
        # If not cached
        email=request.form.get('email').strip().lower()
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()

        # Authentication of user happens here with user and hashed password
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard.dashboard'))

        # If invalid gets redirected to the same page
        else:
            return redirect(url_for('auth.signin'))#---------------add flash here 
        
    # returns to sign page if you try to access this route in not POST method
    return render_template('auth/signin.html')






