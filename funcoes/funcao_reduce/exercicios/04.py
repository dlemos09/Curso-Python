# Objetivo: Usar reduce para concatenar todos os elementos de uma lista de strings.


from functools import reduce

# Lista de strings
strings = ["Olá", "mundo", "Python", "é", "legal"]

# Usando reduce para concatenar as strings
concatenado = reduce(lambda x, y: x + " " + y, strings)

# Exibe o resultado
print(concatenado)  # Saída: Olá mundo Python é legal
