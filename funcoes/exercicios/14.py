# 14. Encontre o Elemento Mais Frequente

def elemento_mais_frequente(lista):
    # Retorna o elemento mais frequente da lista
    frequencias = {}
    for item in lista:
        frequencias[item] = frequencias.get(item, 0) + 1
    return max(frequencias, key=frequencias.get)

# Testando a função
print(elemento_mais_frequente([1, 3, 2, 1, 4, 1, 3, 2, 1]))  # Saída: 1
