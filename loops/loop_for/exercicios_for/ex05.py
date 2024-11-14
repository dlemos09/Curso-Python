# Conta quantas vogais existem em uma string.
frase = (input('Digite uma frase: '))
vogais = "aeiouAEIOUáéôú"
count = 0
for char in frase:
    if char in vogais:
        count += 1
print("Número de vogais:", count)
