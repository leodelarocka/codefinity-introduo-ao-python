# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Deifine função apply_discount

def apply_discount(prices):
    prices_copy = prices.copy()  # Faz copia
    for i in range(len(prices_copy)): # Usa indice [i] sobre q copia
        if prices_copy[i] > 2.00:  # Verifica o valor
            prices_copy[i] *= 0.90  # Aplica 10% de desconto
    return prices_copy  # Retorna o valor atualizado

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)  # Armazena o resultado
print(f"Updated product prices: {product_prices}") # Imprime o resultado