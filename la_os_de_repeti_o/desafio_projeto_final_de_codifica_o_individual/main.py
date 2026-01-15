# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

discount_threshold = 100
min_stock = 30

print(">" * 20)
print("Processing started")
print(">" * 20)

for item in inventory:
    stock, regular_price, discounted_price = inventory[item]
    inventory[item][0] = stock
    if stock > discount_threshold:
        inventory[item][2]
    if stock < min_stock:
        print(f"{item} need restocking.")
    elif stock > discount_threshold:
        print(f"{item} should be sold at the discounted price of {discounted_price}.")
    else:
        print(f"{item} should be sold at the regular price of {regular_price}.")

print("Processing completed")