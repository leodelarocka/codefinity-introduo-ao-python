# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

print("=" * 30)
print("STOCK LEVELS")
print("=" * 30)

#Percorre a lista e imprime o estoque atual
for update in range(len(products)):
    products[update][1] = products[update][1] - units_sold[update][1]
    print(f"Stock levels for item: {update + 1}: {products[update]}") # o print dentro do loop, imprime cada item numerado linha por linha

#Atualizando a lista

print("=" * 30)
print("FINAL STOCK LEVELS")
print("=" * 30)

#Percorre a lista com estoque atual, atuliza somando com produtos recebidos e imprime lista atulizada em uma so linha
for update in range(len(products)):
    products[update][1] = products[update][1] + shipment_received[update][1]
print(f"Final stock levels for all products: {products}") #o print fora do loop imprime em uma so linha
