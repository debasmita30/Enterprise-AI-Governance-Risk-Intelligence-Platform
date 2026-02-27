import sqlite3

def init_db():
    conn = sqlite3.connect("tools.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            security REAL,
            data_residency REAL,
            compliance REAL,
            cost REAL,
            lock_in REAL,
            sla REAL,
            final_score REAL,
            category TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_vendor(data):
    conn = sqlite3.connect("tools.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO vendors 
        (name, security, data_residency, compliance, cost, lock_in, sla, final_score, category)
        VALUES (?,?,?,?,?,?,?,?,?)
    """, (
        data["name"],
        data["security"],
        data["data_residency"],
        data["compliance"],
        data["cost"],
        data["lock_in"],
        data["sla"],
        data["final_score"],
        data["category"]
    ))
    conn.commit()
    conn.close()

def fetch_vendors():
    conn = sqlite3.connect("tools.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vendors")
    rows = cursor.fetchall()
    conn.close()
    return rows