from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '5c96ebe8f6d2240ae73fce62cde38dd9e27faf41ec4da63c'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:14344@localhost/lab_attendance'
    
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    
    from .routes import main
    app.register_blueprint(main)
    
    return app