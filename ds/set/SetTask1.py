events = [
    {"Ahme_Event": ["ram", "amit", "shyam", "ram"]},
    {"Udaipur_Event": ["ram", "amit", "kunal"]},
    {"mumbai_Event": ["ram", "parth", "amit", "ajay", "jay"]}
]

#find who have attended all city event
#find all unique persons
#find who have attended udaipur event but not mumbai's
ahm_data = set(events[0]["Ahme_Event"])
print(ahm_data)
udaipur_data = set(events[1]["Udaipur_Event"])
print(udaipur_data)
mumbai_data = set(events[2]["mumbai_Event"])
print(mumbai_data)

#users_all_attended_events= ahm_data.intersection(udaipur_data).intersection(mumbai_data)
users_all_attended_events = ahm_data & udaipur_data & mumbai_data
print("all ",users_all_attended_events)

#users_all = ahm_data.union(udaipur_data).union(mumbai_data)
users_all = ahm_data | udaipur_data | mumbai_data
print(users_all)

#udaipur_not_mumbai = udaipur_data.difference(mumbai_data)
udaipur_not_mumbai = udaipur_data - mumbai_data
print(udaipur_not_mumbai)