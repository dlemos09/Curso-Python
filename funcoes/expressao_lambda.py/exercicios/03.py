# Lista de pessoas com nome e idade
pessoas = [("Maria", 25), ("João", 30), ("Ana", 22)]

# Ordena por idade usando lambda
pessoas_ordenadas = sorted(pessoas, key=lambda x: x[1])
print(pessoas_ordenadas)  # Saída: [('Ana', 22), ('Maria', 25), ('João', 30)]
