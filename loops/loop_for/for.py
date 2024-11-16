# O comando for em Python é uma estrutura de repetição que permite iterar sobre elementos de uma coleção (como listas, tuplas, dicionários, strings ou outros objetos iteráveis). Sua sintaxe é simples e direta, tornando-o uma ferramenta poderosa para trabalhar com loops.

# Sintaxe Básica

# iteravel = 0

# for variável in iteravel:
#      bloco de código

# Componentes:
# for: Palavra-chave que inicia o laço.
# variável: Nome que representa o elemento atual do iterável durante a iteração. Esse nome é definido pelo programador.
# in: Palavra-chave que conecta o iterável à variável do laço.
# iterável: Um objeto que pode ser iterado, como uma lista, string, tupla, dicionário, ou resultado da função range().
# bloco de código: O conjunto de instruções a ser executado para cada elemento do iterável. Deve estar indentado.

# Exemplo 1: Iterando sobre uma lista

frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)


# Modificadores no for

# break: Interrompe o loop imediatamente.

for i in range(10):
    if i == 5:
        break
    print(i)



# continue: Pula para a próxima iteração.   


for i in range(5):
    if i == 2:
        continue
    print(i)

