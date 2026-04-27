import sqlite3
from datetime import datetime

DB_PATH = '/home/Enzo1401/mysite/data.db'

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS runs 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             date TEXT, passed INTEGER, failed INTEGER, latency REAL)''')

def save_run(passed, failed, latency):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT INTO runs (date, passed, failed, latency) VALUES (?,?,?,?)",
                     (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), passed, failed, latency))

def get_history():
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute("SELECT * FROM runs ORDER BY id DESC LIMIT 10").fetchall()
