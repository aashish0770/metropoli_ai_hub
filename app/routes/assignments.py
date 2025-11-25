from flask import Blueprint, request, jsonify
from sqlalchemy.orm import joinedload
from datetime import datetime

from app.extensions import db
from app.models.assignment import Assignment
from app.models.user import User
from app.models.course import Course

assignments_bp = Blueprint("assignments", __name__)


# ----------------------------
# Create Assignment
# ----------------------------
@assignments_bp.route("/assignments", methods=["POST"])
def create_assignment():
    data = request.get_json() or {}

    required = ["title", "course_id", "student_id"]
    for key in required:
        if key not in data:
            return jsonify({"error": f"'{key}' is required"}), 400

    # Parse deadline
    deadline = None
    if data.get("deadline"):
        try:
            deadline = datetime.strptime(data["deadline"], "%Y-%m-%d %H:%M")
        except ValueError:
            return (
                jsonify({"error": "Deadline must be in 'YYYY-MM-DD HH:MM' format"}),
                400,
            )

    # Validate student & course
    student = User.query.get(data["student_id"])
    if not student:
        return jsonify({"error": "Student not found"}), 404

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
# List Assignments (Teacher)
# ----------------------------
@assignments_bp.route("/assignments", methods=["GET"])
def list_assignments():
    assignments = Assignment.query.options(
        joinedload(Assignment.student), joinedload(Assignment.course)
    ).all()

    return jsonify([a.to_dict() for a in assignments]), 200


