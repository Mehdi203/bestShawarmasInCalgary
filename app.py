import requests
import config

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "shawarma",
    "location": "Calgary"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]

# for b in businesses:
#     print(b["name"])

[print(b["name"]) for b in businesses if b["rating"] > 4]
