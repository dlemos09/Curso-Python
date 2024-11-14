# Exercício 8: Agrupar Valores Iguais
# Escreva um programa que agrupa os valores iguais em um dicionário onde as chaves são categorias e os valores são listas de itens que pertencem a essa categoria.

# Dicionário de exemplo com itens e suas categorias
itens = {"item1": "fruta", "item2": "legume", "item3": "fruta", "item4": "carne", "item5": "legume"}

# Dicionário para armazenar as listas de itens agrupados por categoria
agrupados = {}

# Percorre cada item e sua categoria
for item, categoria in itens.items():
    # Se a categoria já existe no dicionário, adiciona o item à lista
    if categoria in agrupados:
        agrupados[categoria].append(item)
    # Caso contrário, cria uma nova lista com o item
    else:
        agrupados[categoria] = [item]

print("Itens agrupados por categoria:", agrupados)
