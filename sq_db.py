import sqlite3

def create_db():
    conn = sqlite3.connect('sudoku_game.db')
    c = conn.cursor()

    # Create table for player records
    c.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL,
            errors INTEGER NOT NULL,
            moves INTEGER NOT NULL,
            date_recorded TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
    print("Database and table created successfully!")
