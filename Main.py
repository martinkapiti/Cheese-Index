"""
-Walmart
-Kroger
-Target
-Stop and Shop
-Shoprite
-Walgreens

"""


#LOOK FOR OPEN SOURCE PRICE MATCHER


import requests

url = "https://marketplace.walmartapis.com/v3/token"

headers = {
    "Authorization": "Basic eW91cl9pZDp5b3VyX3NlY3JldA==",
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
}

data = {
    "grant_type": "client_credentials",
}

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
print(response.text)


url = "https://marketplace.walmartapis.com/v3/price"
headers = {
    "WM_QOS.CORRELATION_ID": "Correlation_ID",
    "WM_SEC.ACCESS_TOKEN": "Access_Token",
    "WM_SVC.NAME": "Walmart Service Name",
    "accept": "application/json",
    "content-type": "application/json"
}
data = {
    "sku": "SKU_Item",
    "pricing": [
        {
            "currentPriceType": "REDUCED",
            "currentPrice": {
                "currency": "USD",
                "amount": 10
            }
        }
    ]
}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())





"""
# Define the API endpoint URL
api_url = "https://marketplace.walmartapis.com/v3/feeds?feedType=PRICE_AND_PROMOTION"

try:
    # Make the GET request
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response into a Python dictionary
        print("Data fetched successfully:")
        data = response.json()
        print(data)
    else:
        print(f"Error: Request failed with status code {response.status_code}")
        print(response.text) # Print the raw response content for more info
except requests.exceptions.RequestException as e:
    print(f"An error occurred during the request: {e}")

"""



"""
from math import inf # Import infinity as a placeholder value for price comparison

# Dicitonaries representing stores, with each key being a cheese name and each value being a random price
walmart, stopAndShop = {"Cheddar": 1.23, "Mozzarella": 2.76, "Swiss": 2.48, "American": 1.31}, {"Cheddar": 1.26, "Mozzarella": 2.54, "Swiss": 1.06, "American": 2.06}
target, shopRite = {"Cheddar": 1.45, "Mozzarella": 1.26, "Swiss": 1.55, "American": 1.96}, {"Cheddar": 1.33, "Mozzarella": 2.93, "Swiss": 2.88, "American": 2.97}

stores = (walmart, stopAndShop, target, shopRite) # Store each dictionary in a tuple for simple iteration

lowestPrice = inf # Set lowestPrice as the placeholder infinity. Should store the lowest price from of every store

i = 0 # A counter to determine what store has the lowest price (based off of the stores tuple)

while True: # While loop to validate input to look for a specific cheese
    targetCheese = input("Enter a cheese to look for: ").capitalize().strip()
    # Break loop when a valid cheese key from a store is entered. If not, display error message and accept a new input after the error message
    if targetCheese not in walmart.keys(): input(f"Invalid cheese name! Enter either cheese: {', '.join(walmart.keys())}!")
    else: break

for store in stores: # For loop iterates the tuple of store dictionaries
    for name, price in store.items(): # Nested for loop iterates through each store dictionary
        # Checks if the current key in the store is the cheese we are looking for and if its price is less than the currently stored lowestPrice
        if name == targetCheese and price < lowestPrice:
            lowestPrice = price # Set new lowest price
            storeName = "Walmart" if not i else "Stop and Shop" if i == 1 else "Target" if i == 2 else "Shop Rite" # Get the store name of the lowest priced target cheese
    i += 1 # Increment counter

print(f"{storeName} has the cheapest {targetCheese} for ${lowestPrice}!") # Display the result """