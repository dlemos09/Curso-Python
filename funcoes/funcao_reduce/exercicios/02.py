# Objetivo: Calcular a soma de todos os elementos de uma lista utilizando reduce.



from functools import reduce

# Lista de números
numeros = [10, 20, 30, 40]

# Usando reduce para somar todos os números
soma = reduce(lambda x, y: x + y, numeros)

# Exibe o resultado
print(soma)  # Saída: 100
