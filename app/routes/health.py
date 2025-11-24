"""
A very small health-check & basic info endpoint.
This is useful to confirm the app runs after step 1.
"""

from flask import Blueprint, jsonify, current_app

health_bp = Blueprint("health", __name__)


@health_bp.route("/health", methods=["GET"])
def health():
    """
    Return basic health and environment info. Keep it minimal for privacy.
    """
    info = {
        "status": "ok",
        "app": "Metropolia Unified AI Student Support Hub",
        "env": current_app.config.get("ENV"),
        "debug": current_app.config.get("DEBUG"),
        # Do NOT return sensitive info like SECRET_KEY here.
    }
    return jsonify(info), 200
