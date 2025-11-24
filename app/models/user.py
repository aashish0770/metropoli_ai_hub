from datetime import datetime
from app.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), default="student")  # "student" or "teacher"
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship: a user can have many assignments
    assignments = db.relationship("Assignment", back_populates="student")

    def __repr__(self):
        return f"<User {self.email}>"
