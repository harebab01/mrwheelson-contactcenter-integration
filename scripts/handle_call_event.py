import json
from flask import request
from scripts.create_ticket_from_call import create_ticket_for_call

def process_call_event(data):
    print("Incoming call data:", data)
    if data.get('CallDirection') == 'Inbound':
        create_ticket_for_call(data)