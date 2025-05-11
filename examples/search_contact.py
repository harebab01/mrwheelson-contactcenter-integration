import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def find_calls_by_number(number):
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM calls WHERE from_number = %s", (number,))
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    number = input("Voer telefoonnummer in: ")
    matches = find_calls_by_number(number)
    for call in matches:
        print(call)