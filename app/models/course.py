from datetime import datetime
from app.extensions import db


class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship: assignments in this course
    assignments = db.relationship("Assignment", back_populates="course")

    def __repr__(self):
        return f"<Course {self.course_code}>"
