# Student REST API

A simple and professional REST API built with **Python, Flask, and SQLite** for managing student records.

The API supports complete **CRUD operations**:

* Create a student
* Read all students
* Read a student by ID
* Update a student
* Delete a student

## Tech Stack

* Python 3
* Flask
* SQLite
* Pytest
* OpenAPI 3.0
* Makefile

## Project Structure

```text
Student_API/
│
├── app.py
├── openapi.yaml
├── requirements.txt
├── Makefile
├── pytest.ini
├── README.md
├── .gitignore
│
├── migrations/
│   └── 001_create_students.sql
│
└── tests/
    └── test_app.py
```

## API Endpoints

| Method | Endpoint                | Description       |
| ------ | ----------------------- | ----------------- |
| GET    | `/healthcheck`          | Check API health  |
| GET    | `/api/v1/students`      | Get all students  |
| POST   | `/api/v1/students`      | Create a student  |
| GET    | `/api/v1/students/{id}` | Get student by ID |
| PUT    | `/api/v1/students/{id}` | Update student    |
| DELETE | `/api/v1/students/{id}` | Delete student    |

## Requirements

Make sure Python 3 and Git are installed.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/student-rest-api.git
cd student-rest-api
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
make install
```

## Environment Configuration

Create a `.env` file in the project root:

```env
DATABASE_URL=students.db
```

The `.env` file is ignored by Git and should not be committed.

## Database Migration

Create the database table by running:

```bash
make migrate
```

You should see:

```text
Database migration completed successfully!
```

## Run the API

Start the Flask API:

```bash
make run
```

The API will run at:

```text
http://127.0.0.1:5000
```

## Health Check

Test the API:

```bash
curl http://127.0.0.1:5000/healthcheck
```

Expected response:

```json
{
  "status": "healthy"
}
```

## Create a Student

```bash
curl -X POST http://127.0.0.1:5000/api/v1/students \
-H "Content-Type: application/json" \
-d '{
  "name": "Rahul",
  "email": "rahul@gmail.com",
  "age": 25,
  "course": "Data Engineering"
}'
```

## Get All Students

```bash
curl http://127.0.0.1:5000/api/v1/students
```

## Get Student by ID

```bash
curl http://127.0.0.1:5000/api/v1/students/1
```

## Update Student

```bash
curl -X PUT http://127.0.0.1:5000/api/v1/students/1 \
-H "Content-Type: application/json" \
-d '{
  "name": "Rahul",
  "email": "rahul@gmail.com",
  "age": 25,
  "course": "Python"
}'
```

## Delete Student

```bash
curl -X DELETE http://127.0.0.1:5000/api/v1/students/1
```

## Run Tests

Run the unit tests with:

```bash
make test
```

or:

```bash
pytest
```

The tests cover the API endpoints and verify that the API returns the expected HTTP responses.

## OpenAPI Specification

The API documentation is available in:

```text
openapi.yaml
```

This file describes the available endpoints, HTTP methods, request bodies, responses, and data schemas.

## Database Migration

The database schema is stored in:

```text
migrations/001_create_students.sql
```

Run the migration with:

```bash
make migrate
```

## Logging

The application uses Python's logging module with log levels such as:

* INFO
* WARNING

Example:

```text
INFO - Student created successfully
WARNING - Student not found
```

## API Versioning

The API uses versioned endpoints:

```text
/api/v1/students
```

This makes it possible to introduce future versions such as:

```text
/api/v2/students
```

without immediately breaking existing clients.

## License

This project is created for learning and portfolio purposes.
