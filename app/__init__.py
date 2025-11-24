from flask import Flask
from config import BaseConfig
from .extensions import db


def create_app(config_class=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # Health route
    from .routes.health import health_bp

    app.register_blueprint(health_bp, url_prefix="/api")

    # Assignments route
    from .routes.assignments import assignments_bp

    app.register_blueprint(assignments_bp, url_prefix="/api")

    return app
