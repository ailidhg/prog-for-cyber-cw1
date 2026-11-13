# this is a security incident management system
# store and update information about a security incident
incident = {
    "username": "admin",
    "ip_address": "192.168.1.50",
    "event_type": "failed login",
    "risk_level": "high",
}

# show the incident details
print(incident["username"])
print(incident["ip_address"])

incident["status"] = "Under investigation"
print(incident["status"])
incident["risk_level"] = "critical"
print(incident["risk_level"])

# remove the event_type field from the incident
del incident["event_type"]

