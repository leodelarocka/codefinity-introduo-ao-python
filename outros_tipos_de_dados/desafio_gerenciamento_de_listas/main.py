#Lista
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

# Combinando as listas
deli_dept = [meat, cheese, condiment]
print("Initial Deli List: ", deli_dept)

#Reabastecer
if "Ham" in meat and meat[2] < 100:
    meat[2] = 100

#Sazonal
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

#Remover condimento
deli_dept.remove(condiment)

#Ordenar lista
deli_dept.sort()

#Imprimindo
print("Updated Deli List: ", deli_dept)