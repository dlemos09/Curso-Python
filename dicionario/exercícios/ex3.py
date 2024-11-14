# Exercício 3: Mesclar Dois Dicionários e Somar Valores
# Escreva um programa que mescla dois dicionários. Se uma chave aparecer em ambos os dicionários, some os valores associados a essa chave.



# Dois dicionários de exemplo
dicionario1 = {"a": 100, "b": 200, "c": 300}
dicionario2 = {"b": 150, "c": 100, "d": 250}

# Cria uma cópia do primeiro dicionário para evitar alterações indesejadas
dicionario_mesclado = dicionario1.copy()

# Percorre cada chave e valor do segundo dicionário
for chave, valor in dicionario2.items():
    # Se a chave já existe no dicionário mesclado, soma os valores
    if chave in dicionario_mesclado:
        dicionario_mesclado[chave] += valor
    # Se não, adiciona a chave e valor ao dicionário mesclado
    else:
        dicionario_mesclado[chave] = valor

print("Dicionário mesclado:", dicionario_mesclado)
