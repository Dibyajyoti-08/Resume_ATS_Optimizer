import sqlite3

def create_table():
    try:
        conn = sqlite3.connect('resume.db')
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE I NOT EXISTS resumes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phone number TEXT,
                email TEXT,
                secion headers TEXT,
                links TEXT,
                skills TEXT,
                experience TEXT,
                education TEXT,
                num_pages TEXT
            )
        """)

        conn.commit()
        conn.close()
        print("Database Table has been created successfully")
    except Exception as e:
        print(f"Error creating database table: {e}")

def insert_data():
    
    