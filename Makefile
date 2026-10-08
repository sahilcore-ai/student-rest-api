install:
	python3 -m pip install -r requirements.txt

run:
	python3 app.py

migrate:
	python3 -c "import os, sqlite3; from dotenv import load_dotenv; load_dotenv(); conn = sqlite3.connect(os.getenv('DATABASE_URL')); conn.executescript(open('migrations/001_create_students.sql').read()); conn.commit(); conn.close(); print('Database migration completed successfully!')"

test:
	pytest