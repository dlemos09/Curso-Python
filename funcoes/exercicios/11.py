# 11. Números Primos

def eh_primo(numero):
    # Verifica se um número é primo
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Testando a função
print(eh_primo(17))  # Saída: True
print(eh_primo(18))  # Saída: False
