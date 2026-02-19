# FDA Food Recall API Explorer

## User Story
As a user, I want to search FDA food recalls by keyword, state, or hazard classification 
so I can check if a product I bought has been recalled.

## Endpoint
`GET https://api.fda.gov/food/enforcement.json`

## How to run
pip3 install requests
python3 food_recall.py

## Example curl commands
curl "https://api.fda.gov/food/enforcement.json?limit=5"
curl "https://api.fda.gov/food/enforcement.json?search=classification:\"Class+I\"&limit=5"
curl "https://api.fda.gov/food/enforcement.json?count=classification.exact"