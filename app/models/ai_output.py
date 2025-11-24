from datetime import datetime
from app.extensions import db


class AIOutput(db.Model):
    __tablename__ = "ai_outputs"

    id = db.Column(db.Integer, primary_key=True)

    # Store JSON results from AI (plan, complexity, risk, explanation)
    analysis_json = db.Column(db.JSON, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # One-to-one relationship with Assignment
    assignment_id = db.Column(db.Integer, db.ForeignKey("assignments.id"))
    assignment = db.relationship("Assignment", back_populates="ai_output")
    output_json = db.Column(db.Text)

    def __repr__(self):
        return f"<AIOutput assignment={self.assignment_id}>"
