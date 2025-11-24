"""
Entrypoint for local development. Uses the app factory create_app from app.__init__.
Run with:
    python run.py
or
    export FLASK_APP=run.py
    flask run
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    # Simple debug run for development (do not use in production)
    app.run(host="127.0.0.1", port=5000, debug=True)
