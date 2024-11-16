#  Ignorar números pares e exibir apenas os ímpares

# Lista de números de 1 a 10
numeros = list(range(1, 11))

# Percorre cada número na lista
for numero in numeros:
    if numero % 2 == 0:  # Verifica se o número é par
        continue  # Ignora o restante do código para números pares
    print(f"Número ímpar: {numero}")  # Executa apenas para números ímpares
