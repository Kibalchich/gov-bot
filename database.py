import sqlite3

conn = sqlite3.connect('networks.db', check_same_thread=false)
cursor = conn.cursor()

def initDb():
    cursor.execute(''CREATE TABLE IF NOT EXISTS users (
            chat_id INED