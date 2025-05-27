events = [
    {"Ahme_Event": ["ram", "amit", "shyam", "ram"]},
    {"Udaipur_Event": ["ram", "amit", "kunal"]},
    {"mumbai_Event": ["ram", "parth", "amit", "ajay", "jay"]}
]

# Step 1: Convert lists to sets
ahmedabad_attendees = set(events[0]["Ahme_Event"])
udaipur_attendees = set(events[1]["Udaipur_Event"])
mumbai_attendees = set(events[2]["mumbai_Event"])

# 1. Who attended all city events
attended_all = ahmedabad_attendees.intersection(udaipur_attendees).intersection(mumbai_attendees)

# 2. All unique persons
all_unique_persons = ahmedabad_attendees.union(udaipur_attendees).union(mumbai_attendees)

# 3. Attended Udaipur but not Mumbai
udaipur_not_mumbai = udaipur_attendees.difference(mumbai_attendees)

# Print results
print("Attended all city events:", attended_all)
print("All unique persons:", all_unique_persons)
print("Attended Udaipur but not Mumbai:", udaipur_not_mumbai)
