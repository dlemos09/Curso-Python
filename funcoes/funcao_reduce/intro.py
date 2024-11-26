# Função reduce
# A função reduce aplica uma função acumuladora a um iterável, reduzindo-o a um único valor. Está disponível no módulo functools.

# Sintaxe:
    
#     from functools import reduce
# reduce(funcao, iteravel)


from functools import reduce

# Soma acumulada
numeros = [1, 2, 3, 4]
resultado = reduce(lambda x, y: x + y, numeros)
print(resultado)  # Saída: 10
