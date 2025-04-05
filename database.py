import sqlite3

def init_db():
    conn = sqlite3.connect("job_screening.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS candidates (name TEXT, email TEXT, score REAL)")
    conn.commit()
    conn.close()
