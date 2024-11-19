

# 6. Fatorial

def fatorial(n):
    # Calcula o fatorial de um número
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Testando a função
print(fatorial(5))  # Saída: 120
