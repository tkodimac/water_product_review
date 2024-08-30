import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv
load_dotenv()


# Initialize extensions without binding them to an app yet
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'  # Sets the category of login


def create_app():
    """
    Factory function to create and configure the Flask application.

    This function initializes the Flask app, sets up configuration variables,
    initializes extensions, and registers blueprints.

    Returns:
        app (Flask): Configured Flask application instance.
    """

    app = Flask(__name__)  # Create a Flask app instance

    # Set secret key for session management and CSRF protection
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    # Retrieve the database URI from the environment variables
    uri = os.environ.get("DATABASE_URL")
    if uri is None:
        raise ValueError(
            "DATABASE_URL is not set in environment variables."
            )  # Raise an error if DATABASE_URL is not set

    # Handle the older PostgreSQL URI format used by Heroku
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    # Set SQLAlchemy database URI and disable track modifications resources
    app.config["SQLALCHEMY_DATABASE_URI"] = uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with the Flask app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Import and register the main blueprint for routing
    from app.routes import main
    app.register_blueprint(main)

    return app  # Return the configured Flask app instance
