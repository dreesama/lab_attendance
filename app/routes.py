from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from . import db, bcrypt
from .models import User, Laboratory, Computer, Course, Enrollment, Attendance
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return redirect(url_for('main.login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Invalid email or password', 'danger')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        return render_template('admin_dashboard.html')
    elif current_user.role == 'teacher':
        courses = Course.query.filter_by(teacher_id=current_user.id).all()
        return render_template('teacher_dashboard.html', courses=courses)
    else:
        enrollments = Enrollment.query.filter_by(student_id=current_user.id).all()
        return render_template('student_dashboard.html', enrollments=enrollments)

@main.route('/manage/users')
@login_required
def manage_users():
    if current_user.role != 'admin':
        flash('Access denied', 'danger')
        return redirect(url_for('main.dashboard'))
    users = User.query.all()
    return render_template('manage_users.html', users=users)

@main.route('/manage/labs')
@login_required
def manage_labs():
    if current_user.role != 'admin':
        flash('Access denied', 'danger')
        return redirect(url_for('main.dashboard'))
    labs = Laboratory.query.all()
    return render_template('manage_labs.html', labs=labs)

@main.route('/manage/courses')
@login_required
def manage_courses():
    if current_user.role != 'admin':
        flash('Access denied', 'danger')
        return redirect(url_for('main.dashboard'))
    courses = Course.query.all()
    return render_template('manage_courses.html', courses=courses)
