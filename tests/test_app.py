import os
import sqlite3

import pytest

from app import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    test_db = tmp_path / "test_students.db"

    monkeypatch.setenv("DATABASE_URL", str(test_db))

    conn = sqlite3.connect(test_db)

    conn.execute("""
        CREATE TABLE students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER,
            course TEXT
        )
    """)

    conn.commit()
    conn.close()

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_healthcheck(client):
    response = client.get("/healthcheck")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"


def test_add_student(client):
    response = client.post(
        "/api/v1/students",
        json={
            "name": "Rahul",
            "email": "rahul@gmail.com",
            "age": 25,
            "course": "Python"
        }
    )

    assert response.status_code == 201