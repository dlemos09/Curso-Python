
# Exercício 1: Contagem de Frequência de Palavras
# Escreva um programa que conta quantas vezes cada palavra aparece em uma frase fornecida pelo usuário.

frase = input("Digite uma frase: ")

# Inicializa um dicionário para armazenar a contagem de cada palavra
frequencia_palavras = {}

# Divide a frase em palavras e percorre cada uma
for palavra in frase.split():
    # Se a palavra já está no dicionário, incrementa seu valor
    if palavra in frequencia_palavras:
        frequencia_palavras[palavra] += 1
    # Se não, adiciona a palavra ao dicionário com valor 1
    else:
        frequencia_palavras[palavra] = 1

# No código, o Python sabe como atribuir valores às variáveis palavra e contagem porque está usando o método items() do dicionário em um loop for. Aqui está a explicação detalhada:

# O que items() faz?
# O método items() retorna uma visão dos pares chave-valor de um dicionário, onde:

# Cada par é representado como uma tupla (chave, valor).
# Essa tupla pode ser desempacotada diretamente no loop.
    
# # Dicionário simples
# dicionario = {"a": 1, "b": 2, "c": 3}

# # Usando items() no loop
# for chave, valor in dicionario.items():
#     print(f"Chave: {chave}, Valor: {valor}")
# # Saída:
# # Chave: a, Valor: 1
# # Chave: b, Valor: 2
# # Chave: c, Valor: 3