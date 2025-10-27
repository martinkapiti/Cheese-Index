# Cheese
# Created by Brian Mendoza (credit me lol)

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

print(f"{storeName} has the cheapest {targetCheese} for ${lowestPrice}!") # Display the result
