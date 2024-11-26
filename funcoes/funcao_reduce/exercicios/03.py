# Objetivo: Utilizar reduce para encontrar o maior número em uma lista.

from functools import reduce

# Lista de números
numeros = [5, 12, 7, 20, 3]

# Usando reduce para encontrar o maior número
maior_numero = reduce(lambda x, y: x if x > y else y, numeros)

# Exibe o resultado
print(maior_numero)  # Saída: 20
