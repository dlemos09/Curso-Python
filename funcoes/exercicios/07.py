# 7. Contar Vogais

def contar_vogais(texto):
    # Conta o número de vogais em uma string
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

# Testando a função
print(contar_vogais("Programação é incrível!"))  # Saída: 9
