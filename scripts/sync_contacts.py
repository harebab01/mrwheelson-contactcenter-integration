import os
import requests
from mysql.connector import connect
from dotenv import load_dotenv

load_dotenv()

FRESHDESK_API_KEY = os.getenv("FRESHDESK_API_KEY")
FRESHDESK_DOMAIN = os.getenv("FRESHDESK_DOMAIN")

def get_freshdesk_contacts():
    url = f"https://{FRESHDESK_DOMAIN}.freshdesk.com/api/v2/contacts"
    headers = {"Authorization": f"Basic {FRESHDESK_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()

def save_to_db(contacts):
    conn = connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()
    for contact in contacts:
        cursor.execute("""
            INSERT INTO contacts (name, email, phone, freshdesk_id)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE name=%s, email=%s, phone=%s
        """, (
            contact["name"], contact["email"], contact["phone"],
            contact["id"], contact["name"], contact["email"], contact["phone"]
        ))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    contacts = get_freshdesk_contacts()
    save_to_db(contacts)