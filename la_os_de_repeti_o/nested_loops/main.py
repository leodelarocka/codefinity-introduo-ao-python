#Listas Aninhadas - Nested lists
produce = ["Tomatoes", "Lettuce"] # Cria uma lista chamada produce com frutas/vegetais.
dairy = ["Milk", "Cheese"] # Cria uma lista chamada produce com frutas/vegetais.

groceries = [produce, dairy] # Combina as duas listas numa lista maior chamada groceries. Agora groceries é uma lista de duas sublistas.
for section in groceries: # Inicia o laço externo: em cada iteração, section recebe uma das sublistas (produce na 1ª vez, dairy na 2ª).
    for item in section: # Laço interno: percorre cada elemento dentro da sublista atual.
        print(f"Item name: {item}") # Imprime a lista baseada na variavel temporaria aninhada "item" 