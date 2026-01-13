prices = [29.99, 45.50, 12.75, 38.20]
print(f"Number of items subjected to discount: {len(prices)}")

discount = [0.10, 0.20, 0.15, 0.05]

for i in range(len(prices)):
    prices[i] -= prices[i] * discount[i]
    print(f"Updated price for item {i + 1}: ${prices[i]:.2f}")
