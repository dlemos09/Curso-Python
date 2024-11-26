produtos = [{"nome": "Celular", "preco": 1500}, {"nome": "Cadeira", "preco": 250}]
caros = list(filter(lambda p: p["preco"] > 1000, produtos))
print(caros)  # Saída: [{'nome': 'Celular', 'preco': 1500}]
