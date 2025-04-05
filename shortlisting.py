import sqlite3

def store_candidate(name, email, match_score):
    conn = sqlite3.connect("job_screening.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS candidates (name TEXT, email TEXT, score REAL)")
    cur.execute("INSERT INTO candidates VALUES (?, ?, ?)", (name, email, match_score))
    conn.commit()
    conn.close()
