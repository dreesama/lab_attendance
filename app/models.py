from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Laboratory(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    total_pcs = db.Column(db.Integer, nullable=False)
    computers = db.relationship('Computer', backref='laboratory', lazy=True)

class Computer(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    lab_id = db.Column(db.BigInteger, db.ForeignKey('laboratory.id'), nullable=False)
    pc_number = db.Column(db.Integer, nullable=False)
    assigned_student_id = db.Column(db.BigInteger, db.ForeignKey('user.id'))

class Course(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    teacher_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)
    enrollments = db.relationship('Enrollment', backref='course', lazy=True)

class Enrollment(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    course_id = db.Column(db.BigInteger, db.ForeignKey('course.id'), nullable=False)
    student_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)

class Attendance(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    student_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.BigInteger, db.ForeignKey('course.id'), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    time_in = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False)