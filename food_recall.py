import requests

BASE_URL = "https://api.fda.gov/food/enforcement.json"

def get_recalls(keyword=None, state=None, classification=None, limit=5, skip=0):
    search_terms = []
    if keyword:
        search_terms.append(f'product_description:"{keyword}"')
    if state:
        search_terms.append(f'state:"{state}"')
    if classification:
        search_terms.append(f'classification:"{classification}"')

    params = {"limit": limit, "skip": skip}
    if search_terms:
        params["search"] = "+AND+".join(search_terms)

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 404:
        print("No results found.")
        return

    data = response.json()
    print(f"Total results: {data['meta']['results']['total']}\n")

    for r in data["results"]:
        print(f"{r.get('recalling_firm')} | {r.get('classification')} | {r.get('report_date')}")
        print(f"  Product: {r.get('product_description', '')[:80]}")
        print(f"  Reason:  {r.get('reason_for_recall', '')[:80]}")
        print()

# User story: "As a user, I want to search food recalls by keyword, state, or 
# hazard class so I can check if a product I bought has been recalled."

if __name__ == "__main__":
    print("=== Salmonella recalls ===")
    get_recalls(keyword="salmonella", limit=3)

    print("=== Class I recalls in CA ===")
    get_recalls(state="CA", classification="Class I", limit=3)

    print("=== Pagination (skip=5) ===")
    get_recalls(limit=3, skip=5)