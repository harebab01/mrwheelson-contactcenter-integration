import os
import requests
from dotenv import load_dotenv

load_dotenv()

FRESHDESK_API_KEY = os.getenv("FRESHDESK_API_KEY")
FRESHDESK_DOMAIN = os.getenv("FRESHDESK_DOMAIN")

def create_ticket_for_call(call_data):
    url = f"https://{FRESHDESK_DOMAIN}.freshdesk.com/api/v2/tickets"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {FRESHDESK_API_KEY}"
    }
    payload = {
        "description": f"Incoming call from {call_data.get('Number', 'Unknown')}",
        "subject": "Incoming Call",
        "type": "Phone",
        "priority": 1,
        "status": 2
    }
    response = requests.post(url, json=payload, headers=headers)
    print("Ticket created:", response.status_code, response.json())