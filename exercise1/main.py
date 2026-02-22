import requests

url = "https://api.fda.gov/cosmetic/event.json"

params = {
    "search": "report_type:Direct",
    "limit": 10
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    results = data.get("results", [])

    for event in results:
        print(f"Report Number: {event.get('report_number')}")
        print(f"Event Date: {event.get('event_date')}")

        # Patient info 
        patient = event.get("patient", {})
        print(f"Patient Age: {patient.get('age')} {patient.get('age_unit')}")
        print(f"Patient Gender: {patient.get('gender')}")

        # Reactions 
        reactions = event.get("reactions", [])
        print("Reactions:", ", ".join(reactions))

        # Products
        products = event.get("products", [])
        product_names = [p.get("product_name") for p in products]
        print("Products:", ", ".join(product_names))

        print("-" * 50)

else:
    print(f"Failed: {response.status_code}")