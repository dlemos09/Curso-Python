# 3. Par ou Ímpar

num = int(input('Digite um número: '))

def par_ou_impar(numero):
    numero = num
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# Testando a função

retorno = par_ou_impar(num)
print(retorno)  # Saída: Ímpar
