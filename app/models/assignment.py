from datetime import datetime
from app.extensions import db


class Assignment(db.Model):
    __tablename__ = "assignments"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    deadline = db.Column(db.DateTime, nullable=True)
    estimated_hours_per_week = db.Column(db.Integer, default=0)
    stress_level = db.Column(db.Integer, default=0)  # 1–10 scale
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign keys
    student_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))

    # Relationships
    student = db.relationship("User", back_populates="assignments")
    course = db.relationship("Course", back_populates="assignments")
    ai_output = db.relationship(
        "AIOutput", back_populates="assignment", uselist=False, lazy=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline.strftime("%Y-%m-%d %H:%M") if self.deadline else None,
            "estimated_hours_per_week": self.estimated_hours_per_week,
            "stress_level": self.stress_level,
            "student": {
                "id": self.student.id,
                "name": self.student.name,
                "email": self.student.email
            } if self.student else None,
            "course": {
                "id": self.course.id,
                "name": self.course.name,
                "course_code": self.course.course_code
            } if self.course else None
        }
