from app import create_app
from app.extensions import db
from app.models.assignment import Assignment
from datetime import datetime

app = create_app()
with app.app_context():
    # IDs must match existing student & course
    student_id = 1
    course_id = 1

    # Convert deadline string to datetime object
    deadline_dt = datetime.strptime("2025-12-01 23:59", "%Y-%m-%d %H:%M")

    a = Assignment(
        title="Homework 1",
        description="Integrals and derivatives",
        deadline=deadline_dt,
        estimated_hours_per_week=5,
        stress_level=7,
        course_id=course_id,
        student_id=student_id,
    )
    db.session.add(a)
    db.session.commit()
    print("Assignment created:", a.id)
