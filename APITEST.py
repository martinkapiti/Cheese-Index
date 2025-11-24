# You must download the requests package since Python does not come bundled with it
from requests import get

payload = {"api_key": "08c6d2a82a190783415d36df0c3d10ae", "product_id": "15716473"}
r = get("https://api.scraperapi.com/structured/walmart/product/v1", params=payload)

print(r.text)
