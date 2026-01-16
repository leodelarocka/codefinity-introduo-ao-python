# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

# Combinando as 3 listas em 1 lista de Tuplas
combined_list = list(zip(products, prices, quantities_sold))

# Ordenando a lista combinada por ordem alfabetica
sorted_products = sorted(combined_list)

# Imprimindo a lista combinada de produtos
for product_name, price, quantity_sold in sorted_products:
    print(f"Product: {product_name}, Price: {price}, Quantity Sold: {quantity_sold}")
    