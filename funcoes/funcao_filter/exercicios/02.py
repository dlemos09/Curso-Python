palavras = ["oi", "python", "legal", "ok"]
curtas = list(filter(lambda x: len(x) <= 3, palavras))
print(curtas)  # Saída: ['oi', 'ok']
