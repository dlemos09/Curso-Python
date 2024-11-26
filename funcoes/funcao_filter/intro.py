# Função filter
# A função filter retorna elementos de um iterável que atendem a uma condição especificada por uma função.

# filter(funcao, iteravel)

# Filtrando números pares
numeros = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Saída: [2, 4, 6]
