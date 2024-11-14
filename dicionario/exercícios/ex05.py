# Exercício 5: Ordenar um Dicionário por Valores
# Escreva um programa que ordena um dicionário por valores, tanto em ordem crescente quanto decrescente.

# Dicionário de exemplo
dicionario = {"item1": 45, "item2": 10, "item3": 30, "item4": 20}

# Ordena o dicionário por valores em ordem crescente
dicionario_ordenado_crescente = dict(sorted(dicionario.items(), key=lambda item: item[1]))
print("Dicionário em ordem crescente:", dicionario_ordenado_crescente)

# Ordena o dicionário por valores em ordem decrescente
dicionario_ordenado_decrescente = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True))
print("Dicionário em ordem decrescente:", dicionario_ordenado_decrescente)
