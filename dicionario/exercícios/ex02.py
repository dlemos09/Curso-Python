# Exercício 2: Inverter um Dicionário
# Escreva um programa que inverte as chaves e valores de um dicionário, supondo que os valores também são únicos.

# Dicionário original
dicionario_original = {"a": 1, "b": 2, "c": 3, "d": 4}

# Inicializa um novo dicionário para armazenar o invertido
dicionario_invertido = {}

# Percorre cada chave e valor do dicionário original
for chave, valor in dicionario_original.items():
    # Atribui o valor como chave e a chave como valor no novo dicionário
    dicionario_invertido[valor] = chave

print("Dicionário invertido:", dicionario_invertido)
