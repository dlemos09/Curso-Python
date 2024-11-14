
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

# Exibe a contagem de cada palavra
print("Frequência de palavras na frase:")
for palavra, contagem in frequencia_palavras.items():
    print(f"{palavra}: {contagem}")