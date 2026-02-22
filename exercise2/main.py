from fastapi import FastAPI
import httpx
from fastapi import HTTPException

client = httpx.AsyncClient(timeout=10.0)

app = FastAPI()

EXTERNAL_API_URL = "https://api.fda.gov/cosmetic/event.json"

@app.get("/events/summary")
async def get_event_summary(limit: int = 10):
    response = await client.get(
        EXTERNAL_API_URL,
        params={"limit": limit}
    )

    if response.status_code != 200:
        raise HTTPException(status_code = 500, detail="openFDA error")
    
    data = response.json()

    results = []

    for item in data.get("results", []):
        results.append({
            "report_number": item.get("report_number"),
            "age": item.get("patient", {}).get("age"),
            "gender": item.get("patient", {}).get("gender"),
            "reactions": item.get("reactions"),
            "products": [
                p.get("product_name")
                for p in item.get("products", [])
            ]
        })

    return results

