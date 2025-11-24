"""
Configuration file for the Flask app.
We keep a simple BaseConfig for now and read environment variables later as needed.
"""

import os


class BaseConfig:
    ENV = os.environ.get("FLASK_ENV", "development")
    DEBUG = os.environ.get("FLASK_DEBUG", "1") == "1"
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-to-a-secret")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///metropolia_ai_hub.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # AI keys will be set later in env variables (OPENAI_API_KEY, etc.)
