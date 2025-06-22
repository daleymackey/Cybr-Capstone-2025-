import sqlite3
import datetime
import os

DB_NAME = 'honeypot.db'

def init_db():
    """Initialize the database with required tables"""
    conn = sqlite3.connect(DB_NAME)
    
    # Attacks table
    conn.execute('''CREATE TABLE IF NOT EXISTS attacks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        ip_address TEXT NOT NULL,
        username TEXT,
        password TEXT,
        user_agent TEXT,
        attack_type TEXT,
        payload TEXT,
        success INTEGER DEFAULT 0
    )''')
    
    # Sessions table for tracking persistent attackers
    conn.execute('''CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip_address TEXT NOT NULL,
        first_seen TEXT NOT NULL,
        last_seen TEXT NOT NULL,
        attempt_count INTEGER DEFAULT 1
    )''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

def log_attack(ip, username=None, password=None, user_agent=None, attack_type='login_attempt', payload=None):
    """Log an attack attempt"""
    conn = sqlite3.connect(DB_NAME)
    timestamp = datetime.datetime.now().isoformat()
    
    conn.execute('''INSERT INTO attacks 
                    (timestamp, ip_address, username, password, user_agent, attack_type, payload) 
                    VALUES (?, ?, ?, ?, ?, ?, ?)''',
                    (timestamp, ip, username, password, user_agent, attack_type, payload))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()