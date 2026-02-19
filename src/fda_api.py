import requests

search = ""
firstLoop = True

while (search != "Q" and search != "q"):
    search = ""
    firstLoop = True
    while (search!= "event" and search!= "label" and search != "enforcement" and search != "Q" and search != "q"):
        if (firstLoop == False):
            print("""\nMust enter "event", "label", or "enforcement" """)
        search = input("\nWhat would you like to search for? (event, label, or enforcement. Q to quit): ")
        firstLoop = False

    number_searches = -1
    while ((int(number_searches) < 1 or number_searches.isnumeric == False) and search != "Q" and search != "q"):
        number_searches = input("\nHow many results would you like to see?: ")
    
    if (search != "Q" and search != "q"):
        r = requests.get(f'https://api.fda.gov/drug/{search}.json?limit={number_searches}')
        print("Status: ", r.status_code)
        print(r.json())

print("\nThank you for searching with us!")