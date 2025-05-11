import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def log_call(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO calls (call_id, direction, from_number, start_time, duration)
        VALUES (%s, %s, %s, NOW(), %s)
    """, (data['CallId'], data['CallDirection'], data['Number'], data['Duration']))
    conn.commit()
    conn.close()