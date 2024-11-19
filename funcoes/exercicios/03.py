# 3. Par ou Ímpar

def par_ou_impar(numero):
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# Testando a função
print(par_ou_impar(7))  # Saída: Ímpar
