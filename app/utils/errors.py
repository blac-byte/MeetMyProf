from flask import render_template, url_for
import re

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(e):
        return render_template("error/404.html"), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return render_template("error/405.html"), 405

    @app.errorhandler(500)
    def server_error(e):
        return render_template("error/500.html"), 500

def is_student_email(email):
    pattern = r'^[a-zA-Z]+(\.[a-zA-Z]+)?\d{4}@vitstudent\.ac\.in$'
    return bool(re.match(pattern, email))

def is_teacher_email(email):
    pattern = r'^[a-zA-Z]+(\.[a-zA-Z]+)?@vit\.ac\.in$'
    return bool(re.match(pattern, email))