# Soma números dados pelo usuário até que ele digite zero.
soma = 0
numero = int(input("Digite um número (0 para parar): "))
while numero != 0:
    soma += numero
    numero = int(input("Digite um número (0 para parar): "))
print("Soma total:", soma)
