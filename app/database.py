import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "workout.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # workouts（1日分）
    cur.execute("""
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT UNIQUE
        )
    """)

    # exercises（種目）
    cur.execute("""
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workout_id INTEGER,
            name TEXT,
            FOREIGN KEY (workout_id) REFERENCES workouts(id)
        )
    """)

    # sets（セット / 重量・回数）
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise_id INTEGER,
            weight INTEGER,
            reps INTEGER,
            FOREIGN KEY (exercise_id) REFERENCES exercises(id)
        )
    """)

    conn.commit()
    conn.close()
