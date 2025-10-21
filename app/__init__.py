from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .utils.errors import register_error_handlers

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class="app.config.Config"):
    """Application factory pattern"""
    app = Flask(__name__)
    app.config.from_object(config_class)


    # Security configs
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.signin" #------------- redirects here if not logged in


    # Import models so db.create_all() knows them
    from app.models import User, Student, Time, Course, Classes, Teacher, Booking
    with app.app_context():
        db.create_all()
        Time.insert_default_time()
        Course.insert_sample_course()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get((user_id))
        

    # Register blueprints (routes)
    from app.routes.auth import bp as main_routes
    app.register_blueprint(main_routes)

    # Register blueprints (services)
    from app.services.parser import bp as parser
    app.register_blueprint(parser)

    # Register blueprints (services)
    from app.routes.dashboard import bp as dashboard
    app.register_blueprint(dashboard)

    # Register blueprints (routes)
    from app.services.booking import bp as booking
    app.register_blueprint(booking)

    # Register blueprints (routes)
    from app.routes.logout import bp as logout
    app.register_blueprint(logout)

    # Error handlers
    from app.utils.errors import register_error_handlers
    register_error_handlers(app)

    return app
