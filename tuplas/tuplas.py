"""

O que são Tuplas em Python?

As tuplas são um tipo de estrutura de dados em Python semelhante a uma lista, mas com uma diferença crucial: elas são imutáveis. Isso significa que, uma vez criada, uma tupla não pode ser modificada (ou seja, não é possível adicionar, remover ou alterar elementos nela).

Características das Tuplas
São definidas usando parênteses ().
Aceitam diferentes tipos de dados.
Podem ser indexadas e permitem slicing (fatiamento).
São eficientes para armazenar dados que não precisam ser alterados.
Quando usar tuplas?
Tuplas são úteis quando queremos garantir que os dados permanecerão constantes durante a execução do programa. São ideais para representar informações que não mudam, como coordenadas (x, y), constantes matemáticas (π, e), e dias da semana.

"""


#tupla = tuple()
#tupla = (10,)
#tupla = ("Jamilton",)
tupla = ("Jamilton", "Pedro", "Ana", "João", "Pedro")
#print(type(tupla))
#print(tupla[0])
#print(tupla[-1])
#print(tupla[0:2])
#print(tupla[::-1])

#tupla[0] = "alterado"
#print(len(tupla))
#print(tupla.index("Pedro"))
print(tupla.count("Pedro"))
# print(tupla)