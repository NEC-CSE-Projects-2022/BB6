import sqlite3
import os

def get_db_path():
    # data/college.db (relative to this file)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    return os.path.join(data_dir, "college.db")

def init_db():
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Drop tables if they already exist (for re-run safety)
    cur.execute("DROP TABLE IF EXISTS enrollments;")
    cur.execute("DROP TABLE IF EXISTS students;")
    cur.execute("DROP TABLE IF EXISTS courses;")

    # Create tables
    cur.execute("""
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            cgpa REAL NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE courses (
            id INTEGER PRIMARY KEY,
            course_name TEXT NOT NULL,
            credits INTEGER NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE enrollments (
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            grade TEXT,
            FOREIGN KEY(student_id) REFERENCES students(id),
            FOREIGN KEY(course_id) REFERENCES courses(id)
        );
    """)

    # Insert sample students
    students_data = [
        (1, "Anil Kumar",    "CSE", 8.4),
        (2, "Bhavya Reddy",  "CSE", 9.1),
        (3, "Charan Teja",   "ECE", 7.8),
        (4, "Deepika Rao",   "EEE", 8.9),
        (5, "Farhan Ali",    "MECH",7.2),
        (6, "Gowtham",       "CSE", 8.0),
        (7, "Harika",        "IT",  9.0),
        (8, "Ishaan",        "CIVIL",7.5),
        (9, "Jyothi",        "ECE", 8.6),
        (10,"Karthik",       "IT",  8.2),
    ]

    cur.executemany(
        "INSERT INTO students (id, name, department, cgpa) VALUES (?, ?, ?, ?);",
        students_data
    )

    # Insert sample courses
    courses_data = [
        (1, "Database Systems", 4),
        (2, "Data Structures",  3),
        (3, "Operating Systems",4),
        (4, "Computer Networks",3),
        (5, "Machine Learning", 4),
        (6, "Digital Electronics",3),
        (7, "Linear Algebra",   3),
        (8, "Software Engineering",3),
    ]

    cur.executemany(
        "INSERT INTO courses (id, course_name, credits) VALUES (?, ?, ?);",
        courses_data
    )

    # Insert sample enrollments
    enrollments_data = [
        (1, 1, "A"),
        (1, 2, "A"),
        (1, 5, "B"),
        (2, 1, "A"),
        (2, 5, "A"),
        (3, 2, "B"),
        (3, 6, "A"),
        (4, 1, "A"),
        (4, 3, "A"),
        (5, 2, "C"),
        (5, 4, "B"),
        (6, 1, "B"),
        (6, 2, "B"),
        (7, 5, "A"),
        (7, 8, "A"),
        (8, 4, "B"),
        (9, 6, "A"),
        (9, 7, "B"),
        (10,1, "B"),
        (10,3, "A"),
    ]

    cur.executemany(
        "INSERT INTO enrollments (student_id, course_id, grade) VALUES (?, ?, ?);",
        enrollments_data
    )

    conn.commit()
    conn.close()
    print(f"Database initialized at: {db_path}")

if __name__ == "__main__":
    init_db()
