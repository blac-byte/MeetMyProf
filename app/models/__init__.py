# app/models/__init__.py
from .user import User
from .student import Student
from .time import Time
from .classes import Classes
from .course import Course
from .teacher import Teacher


__all__ = ["User", "Student", "Teacher", "Time", "Classes", "Course"]
