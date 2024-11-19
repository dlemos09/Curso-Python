# 13. Ordenação de Lista

def ordenar_lista(lista):
    # Ordena uma lista em ordem crescente (implementação manual)
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

# Testando a função
print(ordenar_lista([4, 2, 9, 1, 5]))  # Saída: [1, 2, 4, 5, 9]
