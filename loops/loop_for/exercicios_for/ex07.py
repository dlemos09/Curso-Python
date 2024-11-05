# Calcula o fatorial de um número n usando for.
n = int(input("Digite um número: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print(f"Fatorial de {n} é {fatorial}")
