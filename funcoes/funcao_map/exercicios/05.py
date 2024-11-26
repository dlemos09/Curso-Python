dados = [50, 200, 150, 100]
total = sum(dados)
normalizado = list(map(lambda x: x / total, dados))
print(normalizado)  # Saída: [0.1, 0.4, 0.3, 0.2]
