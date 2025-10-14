# app/models/__init__.py
from .user import User
from .student import Student
from .time import Time
from .classes import Classes
from .course import Course
from .teacher import Teacher
from .booking import Booking
from .slot import Slot

__all__ = ["User", "Student", "Teacher", "Time", "Classes", "Course", "Booking", "Slot"]
