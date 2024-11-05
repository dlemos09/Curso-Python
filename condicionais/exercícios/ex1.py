# Solicita um número do usuário e verifica se é par ou ímpar.
num = int(input("Digite um número: "))
if num % 2 == 0:
    print(f'O número é par, você digitou {num}')
else:
    print(f'O número é impar, você digitou {num}')