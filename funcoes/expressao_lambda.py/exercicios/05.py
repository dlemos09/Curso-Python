from functools import reduce

# Usando lambda para soma acumulada
numeros = [10, 20, 30]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)  # Saída: 60
