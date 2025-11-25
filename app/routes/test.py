from flask import Blueprint, jsonify
from app.services.ai_service import analyze_assignment_stub

test_bp = Blueprint("test", __name__)


@test_bp.route("/test-ai")
def test_ai():
    return jsonify(analyze_assignment_stub("hello"))
