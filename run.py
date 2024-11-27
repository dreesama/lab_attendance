from app import create_app, db
from app.models import User
from flask_bcrypt import Bcrypt

app = create_app()
bcrypt = Bcrypt(app)

def init_db():
    try:
        with app.app_context():
            # Create all database tables
            db.create_all()
            
            # Check if admin user exists
            admin = User.query.filter_by(email='admin@example.com').first()
            if not admin:
                # Create admin user
                hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
                admin = User(
                    name='Admin User',
                    email='admin@example.com',
                    password=hashed_password,
                    role='admin'
                )
                db.session.add(admin)
                db.session.commit()
                print('Admin user created successfully!')
    except Exception as e:
        print(f"Error initializing database: {str(e)}")
        raise e

if __name__ == '__main__':
    init_db()  # Initialize database and create admin user
    app.run(debug=True)