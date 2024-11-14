# Exercício 7: Remover Itens de um Dicionário com Base em uma Condição
# Escreva um programa que remove todos os itens de um dicionário cujos valores estão abaixo de um valor limite.

# Dicionário de exemplo com produtos e preços
precos = {"produto1": 5, "produto2": 15, "produto3": 25, "produto4": 10}

# Define o limite para remoção
limite = 10

# Usa compreensão de dicionário para criar um novo dicionário com valores acima do limite
precos_filtrados = {produto: preco for produto, preco in precos.items() if preco >= limite}

print("Dicionário após remoção dos itens abaixo do limite:", precos_filtrados)
