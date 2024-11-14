# Exercício 6: Criar um Dicionário Aninhado com Contagem de Caracteres
# Escreva um programa que conta a ocorrência de cada letra em várias palavras, retornando um dicionário aninhado onde cada palavra é uma chave, e seu valor é outro dicionário com a contagem de cada letra.

# Lista de palavras para analisar
palavras = ["banana", "maçã", "laranja"]

# Inicializa o dicionário aninhado
contagem_letras = {}

# Percorre cada palavra na lista
for palavra in palavras:
    # Cria um dicionário para contar as letras da palavra atual
    letras = {}
    for letra in palavra:
        # Incrementa a contagem da letra no dicionário
        letras[letra] = letras.get(letra, 0) + 1
    # Adiciona o dicionário de contagem de letras ao dicionário principal
    contagem_letras[palavra] = letras

print("Contagem de letras em cada palavra:", contagem_letras)
