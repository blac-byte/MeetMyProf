# app/services/parser.py

from flask import request, Blueprint, url_for, redirect, render_template, flash
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from flask_login import login_required, current_user
from ..models import Classes
from app import db
from ..utils.errors import register_error_handlers

bp=Blueprint('parser', __name__)

@bp.route('/parser', methods=['GET','POST'])
@login_required
def parser():
    return render_template('parser.html')

#__________________________________________________________________________

# db inserts need to check for duplicate entries

@bp.route('/parser_check', methods=['POST'])
@login_required
def parser_check():
    
    if request.method=='POST':
        user_id=current_user.get_id()
        theory={}
        lab={}
        
        # gets the copy-pasted timetable
        raw_text=request.form.get('table')
        rows=raw_text.splitlines()
        
        day=None
        for row in rows:
            part=row.split('\t')
            # Only takes the class slots, ignoring the theory and lab time slot strips
            # since they are universal and admin controlled db table
            
            if part[0].strip() in ['MON','TUE','WED','THU','FRI','SAT','SUN']:
                 day=part[0].strip()
                 theory[day] = [item.strip() for item in part[2:] if item.strip() != 'Lunch']
                 # ['A1', 'F1', 'D1', 'TB1', 'TG1', '-', 'Lunch', 'A2-BAEEE101-ETH-PRP105-ALL03', 'F2', 'D2-BACSE103-ETH-PRP105-ALL03', 'TB2-BAMAT101-ETH-PRP105-ALL03', 'TG2-BACHY105-ETH-PRP105-ALL03', '-', 'V3']
                 # ['B1', 'G1', 'E1', 'TC1', 'TAA1', '-', 'Lunch', 'B2-BAMAT101-ETH-PRP105-ALL03', 'G2-BACHY105-ETH-PRP105-ALL03', 'E2', 'TC2', 'TAA2', '-', 'V4']
                 # ['C1', 'A1', 'F1', 'V1', 'V2', '-', 'Lunch', 'C2', 'A2-BAEEE101-ETH-PRP105-ALL03', 'F2', 'TD2-BACSE103-ETH-PRP105-ALL03', 'TBB2', '-', 'V5']
                 # ['D1', 'B1', 'G1', 'TE1', 'TCC1', '-', 'Lunch', 'D2-BACSE103-ETH-PRP105-ALL03', 'B2-BAMAT101-ETH-PRP105-ALL03', 'G2-BACHY105-ETH-PRP105-ALL03', 'TE2', 'TCC2', '-', 'V6']
                 # ['E1', 'C1', 'TA1', 'TF1', 'TD1', '-', 'Lunch', 'E2', 'C2', 'TA2-BAEEE101-ETH-PRP105-ALL03', 'TF2', 'TDD2', '-', 'V7']      
                 # ['V8', 'X11', 'X12', 'Y11', 'Y12', '-', 'Lunch', 'X21', 'Z21', 'Y21', 'W21', 'W22', '-', 'V9']
                 # ['V10', 'Y11', 'Y12', 'X11', 'X12', '-', 'Lunch', 'Y21', 'Z21', 'X21', 'W21', 'W22', '-', 'V11']
            

            elif part[0].strip()=='LAB' and day is not None:
                lab[day] = [item.strip() for item in part[1:] if item.strip() != 'Lunch']
                 # ['L1', 'L2', 'L3-BAMAT101-ELA-PRP445-ALL03', 'L4-BAMAT101-ELA-PRP445-ALL03', 'L5', 'L6', 'Lunch', 'L31', 'L32', 'L33', 'L34', 'L35', 'L36', '-']
                 # ['L7-BACSE101-LO-PRP117a-ALL03', 'L8-BACSE101-LO-PRP117a-ALL03', 'L9', 'L10', 'L11', 'L12', 'Lunch', 'L37', 'L38', 'L39', 'L40', 'L41', 'L42', '-']
                 # ['L13-BACHY105-ELA-PRPG07-ALL03', 'L14-BACHY105-ELA-PRPG07-ALL03', 'L15-BACSE103-ELA-PRP356-ALL03', 'L16-BACSE103-ELA-PRP356-ALL03', 'L17', 'L18', 'Lunch', 'L43', 'L44', 'L45', 'L46', 'L47', 'L48', '-']
                 # ['L25-BAEEE101-ELA-PRP355-ALL03', 'L26-BAEEE101-ELA-PRP355-ALL03', 'L27-BACSE101-LO-PRP117a-ALL03', 'L28-BACSE101-LO-PRP117a-ALL03', 'L29', 'L30', 'Lunch', 'L55', 'L56', 'L57', 'L58', 'L59', 'L60', '-']
                 # ['L71', 'L72', 'L73', 'L74', 'L75', 'L76', 'Lunch', 'L77', 'L78', 'L79', 'L80', 'L81', 'L82', '-']
                 # ['L83', 'L84', 'L85', 'L86', 'L87', 'L88', 'Lunch', 'L89', 'L90', 'L91', 'L92', 'L93', 'L94', '-']


#-------------------------------------------------------------------------------------
        commit_log=set()
        
        for day in theory:
          try:
               for column_id, (part_theory, part_lab) in enumerate(zip(theory[day], lab[day])):
                    if part_theory.count('-')>1:
                         
                         parts=part_theory.split('-')
                         unique_log=(user_id, parts[0].strip(), day)

                         if unique_log not in commit_log:
                              commit_log.add(unique_log)
                              db.session.add(Classes(user_id, parts[1], parts[2], day, column_id, parts[0]))

                    if part_lab.count('-')>1:
                         
                         parts=part_lab.split('-')
                         unique_log=(user_id, parts[0], day)
                         
                         if unique_log not in commit_log:
                              commit_log.add(unique_log)
                              db.session.add(Classes(user_id, parts[1], 'ELA', day, column_id, parts[0]))

          except SQLAlchemyError as e:
          # Rollback for other database errors
               db.session.rollback()
               flash(f'An error occurred: {str(e)}')
               return register_error_handlers.server_error()

          except IntegrityError:
               # Rollback session in case of database integrity error
               db.session.rollback()
               flash('Integrity error occurred. Please check your data.')
               return register_error_handlers.server_error()


        db.session.commit()
        
        return redirect(url_for('dashboard.dashboard'))

    return redirect(url_for('auth.signin'))