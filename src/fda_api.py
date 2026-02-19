import requests

search = ""
firstLoop = True

while (search != "Q"):
    search = ""
    firstLoop = True
    while (search!= "event" and search!= "label" and search != "enforcement"):
        if (firstLoop == False):
            print("""Must enter "event", "label", or "enforcement" """)
        search = input("What would you like to search for? (event, label, or enforcement. Q to quit): ")
        firstLoop = False

    if (search == "event"):
        r = requests.get('https://api.fda.gov/drug/event.json?limit=1')
    elif (search == "label"):
        r = requests.get('https://api.fda.gov/drug/label.json?limit=1')
    elif (search == "enforcement"):
        r = requests.get('https://api.fda.gov/drug/enforcement.json?limit=1')
    if (search != "Q"):
        print("Status: ", r.status_code)
        print(r.json())

print("\nThank you for searching with us!")