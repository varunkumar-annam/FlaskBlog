
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# import secrets



# # def create_app():
# app = Flask(__name__)

# # Generating secret key to protect against modifying cookies, cross-site requests, and forgery attacks
# app.config['SECRET_KEY'] = secrets.token_hex(16)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# db = SQLAlchemy(app)
# bcrypt=Bcrypt(app)
# # Initialize the database with the app
# # db.init_app(app)
# from flaskblog.models import User,Post
# with app.app_context():
    
#     db.create_all()  # Create the database tables within the app context

    
# from flaskblog import routes    

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import secrets

db = SQLAlchemy()


# def create_app():
app = Flask(__name__)

# Generate a secret key to protect against modifying cookies, cross-site requests, and forgery attacks
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Initialize the database with the app
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

with app.app_context():
    from flaskblog.models import User,Post  # Import models to ensure they're registered with SQLAlchemy
    db.create_all()  # Create the database tables within the app context

# Import routes here (after the app is initialized)
from flaskblog import routes

# return app
