# Exercício 4: Filtrar um Dicionário por Valores Acima de um Limite
# Crie um programa que filtra um dicionário, retornando apenas os itens cujo valor é maior que um limite definido pelo usuário.

# Dicionário de exemplo
produtos = {"produto1": 20, "produto2": 55, "produto3": 35, "produto4": 70}

# Pede ao usuário para definir o valor limite
limite = int(input("Digite o valor limite: "))

# Usa uma compreensão de dicionário para filtrar os itens com valor acima do limite
produtos_filtrados = {produto: preco for produto, preco in produtos.items() if preco > limite}

print("Produtos com valor acima do limite:", produtos_filtrados)
