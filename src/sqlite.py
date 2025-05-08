import sqlite3

def create_table():
    try:
        conn = sqlite3.connect('resumes.db')
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS resumes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phone_number TEXT,
                email TEXT,
                section_headers TEXT,
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

def insert_data(data):
    try:
        conn = sqlite3.connect("resumes.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO resumes (phone_number, email, section_headers, links,
            skills, experience, education, num_pages)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["phone_number"],
            data["email"],
            data["section_headers"],
            data["links"],
            data["skills"],
            data["experience"],
            data["education"],
            data["num_pages"]
        ))

        conn.commit()
        conn.close()
        print("Data inserted successfully into the database.")
    except Exception as e:
        print(f"Error inserting data into the database: {e}")
    