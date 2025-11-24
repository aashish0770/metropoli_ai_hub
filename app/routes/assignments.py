from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.assignment import Assignment
from app.models.user import User
from app.models.course import Course
from datetime import datetime

assignments_bp = Blueprint("assignments", __name__)


# ----------------------------
# Student: Create a new assignment
# ----------------------------
@assignments_bp.route("/assignments", methods=["POST"])
def create_assignment():
    """
    Sample JSON body:
    {
        "title": "Math Homework 1",
        "description": "Integrals and derivatives",
        "deadline": "2025-12-01 23:59",
        "estimated_hours_per_week": 5,
        "stress_level": 7,
        "course_id": 1,
        "student_id": 1
    }
    """
    data = request.get_json()

    # Validation
    required_fields = ["title", "course_id", "student_id"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    # Convert deadline string to datetime
    deadline = None
    if "deadline" in data and data["deadline"]:
        try:
            deadline = datetime.strptime(data["deadline"], "%Y-%m-%d %H:%M")
        except ValueError:
            return (
                jsonify({"error": "Invalid deadline format. Use YYYY-MM-DD HH:MM"}),
                400,
            )

    # Check if student exists
    student = User.query.get(data["student_id"])
    if not student:
        return jsonify({"error": "Student not found"}), 404

    # Check if course exists
    course = Course.query.get(data["course_id"])
    if not course:
        return jsonify({"error": "Course not found"}), 404

    # Create assignment
    assignment = Assignment(
        title=data["title"],
        description=data.get("description"),
        deadline=deadline,
        estimated_hours_per_week=data.get("estimated_hours_per_week", 0),
        stress_level=data.get("stress_level", 0),
        student_id=student.id,
        course_id=course.id,
    )

    db.session.add(assignment)
    db.session.commit()

    return (
        jsonify(
            {
                "message": "Assignment created successfully",
                "assignment_id": assignment.id,
            }
        ),
        201,
    )


# ----------------------------
# Teacher: List all assignments (read-only)
# ----------------------------
@assignments_bp.route("/assignments", methods=["GET"])
def list_assignments():
    assignments = Assignment.query.all()
    return jsonify([a.to_dict() for a in assignments]), 200
