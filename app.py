
import os
import sqlite3
import logging

from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = Flask(__name__)


# Database connection
def get_db_connection():
    database_url = os.getenv("DATABASE_URL")

    conn = sqlite3.connect(database_url)
    conn.row_factory = sqlite3.Row
    return conn


# Home
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Student API is running successfully!"
    })

# Healthcheck
@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({
        "status": "healthy"
    })


# Get all students
@app.route("/api/v1/students", methods=["GET"])
def get_students():
    conn = get_db_connection()

    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()

    conn.close()

    return jsonify([
        dict(student) for student in students
    ])


# Add student
@app.route("/api/v1/students", methods=["POST"])
def add_student():
    data = request.get_json()

    conn = get_db_connection()

    conn.execute(
        "INSERT INTO students (name, email, age, course) VALUES (?, ?, ?, ?)",
        (
            data["name"],
            data["email"],
            data["age"],
            data["course"]
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student added successfully"
    }), 201


# Get student by ID
@app.route("/api/v1/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    conn.close()

    if student is None:
        return jsonify({
            "message": "Student not found"
        }), 404

    return jsonify(dict(student))


# Update student
@app.route("/api/v1/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()

    conn = get_db_connection()

    conn.execute(
        """
        UPDATE students
        SET name = ?, email = ?, age = ?, course = ?
        WHERE id = ?
        """,
        (
            data["name"],
            data["email"],
            data["age"],
            data["course"],
            student_id
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student updated successfully"
    })


# Delete student
@app.route("/api/v1/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    conn = get_db_connection()

    conn.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student deleted successfully"
    })


# Start Flask
if __name__ == "__main__":
    app.run(debug=True)

