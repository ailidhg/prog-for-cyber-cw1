# Security Event Logger
# import necessary libraries
import random
import socket
from datetime import datetime

username = "admin"
password = "UWS756"
event_log = []

# generate a random event ID and log the event with timestamp and IP address
while True:
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")
    event_id = random.randint(1000, 9999)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if username_input == username and password_input == password:
        print("Access granted.")
        event_log.append({
            "username": username_input,
            "event": "successful login",
            "timestamp": timestamp,
            "event_id": event_id,
            "ip_address": ip_address

        })
        break
    else:
        print("Failed login attempt.")
        event_log.append({
            "username": username_input,
            "event": "failed login",
            "timestamp": timestamp,
            "event_id": event_id,
            "ip_address": ip_address
        })

# print the event log
for event in event_log:
    print(f"Event ID: {event['event_id']}, Username: {event['username']}, Event: {event['event']}, Timestamp: {event['timestamp']}, IP Address: {event['ip_address']}")