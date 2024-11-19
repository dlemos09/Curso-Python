# 9. Sequência de Fibonacci

def fibonacci(n):
    # Gera os primeiros n números da sequência de Fibonacci
    sequencia = [0, 1]
    for i in range(2, n):
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia[:n]

# Testando a função
print(fibonacci(10))  # Saída: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
