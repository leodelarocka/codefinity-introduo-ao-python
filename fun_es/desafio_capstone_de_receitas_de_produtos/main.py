# Define a function to calculate the revenue for each product
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for price, qty in zip(prices, quantities_sold):
        revenue.append(price * qty)
    return revenue

# Define a function to format and display the sorted revenues
def formatted_output(revenues):
    revenues_sorted = sorted(revenues, key=lambda x: x[0])
    for prod, rev in revenues_sorted:
        print(f"{prod} has total revenue of ${rev}")

# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]
quantities_sold = [150, 200, 100, 50]

# Execute as pedido
revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))
formatted_output(revenue_per_product)