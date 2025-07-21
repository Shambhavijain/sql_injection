# init_db.py
import sqlite3

def init_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create candidates table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        );
    """)

    # Create votes table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS votes (
            user_id TEXT NOT NULL,
            candidate_id TEXT NOT NULL,
            vote_count INTEGER NOT NULL,
            PRIMARY KEY (user_id, candidate_id)
        );
    """)

    #  Insert some initial candidates
    cursor.execute("INSERT OR IGNORE INTO candidates (id, name) VALUES (1, 'Alice');")
    cursor.execute("INSERT OR IGNORE INTO candidates (id, name) VALUES (2, 'Bob');")
    cursor.execute("INSERT OR IGNORE INTO candidates (id, name) VALUES (3, 'Charlie');")

    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == '__main__':
    init_database()