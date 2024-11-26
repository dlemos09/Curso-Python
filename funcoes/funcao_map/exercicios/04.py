nomes = ["Ana", "João", "Maria"]
idades = [22, 30, 25]
pessoas = list(map(lambda nome, idade: {"nome": nome, "idade": idade}, nomes, idades))
print(pessoas)
# Saída: [{'nome': 'Ana', 'idade': 22}, {'nome': 'João', 'idade': 30}, {'nome': 'Maria', 'idade': 25}]
