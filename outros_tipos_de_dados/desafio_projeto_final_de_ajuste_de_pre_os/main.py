#criar dicionário
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

#verificar e atulizar preço
eggs_price = grocery_inventory["Eggs"][1]
print ("Eggs Price:", eggs_price)
if eggs_price > 5:
    grocery_inventory["Eggs"] = ("Dairy", eggs_price -1, 30)
    print("eggs are too expensive, reducing the price by $1.")
else:
    print ("The price of Eggs are reasonable.")

#Adicionar um novo item
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:", grocery_inventory)

#verificar estoque de milk
milk_stock = grocery_inventory["Milk"][2]
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock")
grocery_inventory.update({
    "Milk": ("Dairy", 3.50, milk_stock + 20)
})

#Remover item com base no preço (apples)
apples_price = grocery_inventory["Apples"][1]
if apples_price > 2:
    grocery_inventory.pop()

print("Updated inventory:", grocery_inventory)