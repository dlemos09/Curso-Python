"""
set -> Conjunto
"""


# Operações Básicas com Conjuntos
# Conjuntos permitem operações matemáticas de união, interseção e diferença:

# 1. União (| ou union()): Retorna um novo conjunto com todos os elementos de ambos os conjuntos.

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Saída: {1, 2, 3, 4, 5}
print(a.union(b))  # Saída: {1, 2, 3, 4, 5}

# 2. Interseção (& ou intersection()): Retorna um novo conjunto com os elementos comuns aos dois conjuntos.

print(a & b)  # Saída: {3}
print(a.intersection(b))  # Saída: {3}

# 3. Diferença (- ou difference()): Retorna um novo conjunto com os elementos que estão apenas em um dos conjuntos.

print(a - b)  # Saída: {1, 2} (elementos que estão em 'a' mas não em 'b')
print(b - a)  # Saída: {4, 5} (elementos que estão em 'b' mas não em 'a')

# 4. Diferença Simétrica (^ ou symmetric_difference()): Retorna um novo conjunto com os elementos que estão em um ou outro conjunto, mas não em ambos.

print(a ^ b)  # Saída: {1, 2, 4, 5}
print(a.symmetric_difference(b))  # Saída: {1, 2, 4, 5}


# Métodos Úteis dos Conjuntos
# Além das operações matemáticas, conjuntos têm métodos úteis:
    
#     add(): Adiciona um elemento ao conjunto.

conjunto = {1, 2, 3}
conjunto.add(4)
print(conjunto)  # Saída: {1, 2, 3, 4}

# remove(): Remove um elemento do conjunto; gera um erro se o elemento não existir.


conjunto.remove(3)
print(conjunto)  # Saída: {1, 2, 4}

# discard(): Remove um elemento do conjunto; não gera erro se o elemento não existir.

conjunto.discard(5)  # Não gera erro



# clear(): Remove todos os elementos do conjunto.
conjunto.clear()
print(conjunto)  # Saída: set()



#lista = ["Jamilton", "José", "Ana", "Ana"]
itens = {"Jamilton", "José", "Ana"}
#print(type(itens))
#print(itens)

carros = {"fusca", "gol", "fiat 147"}
carros2 = {"BMW", "fusca", "passat"}
#novo = carros.union(carros2)
novo = carros.intersection(carros2)
print(novo)
#carros.add("BMW")
#carros.remove("fusca")
# print(carros)

# Exemplo de Uso: Remover Duplicatas de uma Lista
# Um dos usos mais comuns de conjuntos é eliminar duplicatas em uma lista.


lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5]
conjunto = set(lista_com_duplicatas)  # Converte para conjunto para remover duplicatas
lista_sem_duplicatas = list(conjunto)  # Converte de volta para lista
print(lista_sem_duplicatas)  # Saída: [1, 2, 3, 4, 5]
