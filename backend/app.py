# Import the required libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from sqlalchemy import true

from flask_jwt_extended import JWTManager

from datetime import datetime, timedelta, timezone

# Create various application instances
# Order matters: Initialize SQLAlchemy before Marshmallow
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()


def create_app():
    """Application-factory pattern"""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # for login
    app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
    # jwt = JWTManager(app)
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

    # Initialize extensions
    # To use the application instances above, instantiate with an application:
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app)

    return app
