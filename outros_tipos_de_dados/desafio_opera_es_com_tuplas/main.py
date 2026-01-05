# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

#Contar quantas vezes apples aparecem na tupla shelf
apple_count = shelf.count("apples")
print("Number of Apples:", apple_count)

banana_index = shelf.index("bananas")
print("First Banana Index:", banana_index)

#Verificar se o numero de apples é < 5 e se for verdadeiro ou falso, imprima:
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

#Status de grapes
grape_count = shelf.count("grapes")
if grape_count >= 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

#Procurando orange
oranges_index = shelf.index("oranges")
if "oranges" in shelf:
    print("Oranges are at index:", oranges_index)
else:
    print("Oranges are out of stock.")




