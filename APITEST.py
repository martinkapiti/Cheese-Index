# import requests

# payload = { 'api_key': '08c6d2a82a190783415d36df0c3d10ae', 'url': 'https://www.walmart.com/shop/deals/flash-deals?clickid=Q3N0enT5dxycUyA0Xj398wN3UkpW1JQq33oNwI0&irgwc=1&afsrc=1&sourceid=imp_Q3N0enT5dxycUyA0Xj398wN3UkpW1JQq33oNwI0&veh=aff&wmlspartner=imp_2091438&affiliates_ad_id=1167790&campaign_id=9383&sharedid=SiteSuggest', 'output_format': 'json', 'autoparse': 'true' }
# r = requests.get('https://api.scraperapi.com/', params=payload)
# print(r.text)


import requests

payload = { 'api_key': '08c6d2a82a190783415d36df0c3d10ae', 'product_id': '15716473' }
r = requests.get('https://api.scraperapi.com/structured/walmart/product/v1', params=payload)
print(r.text)
