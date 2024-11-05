# Recebe três lados e verifica se podem formar um triângulo.
a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))
if a + b > c and a + c > b and b + c > a:
    print("Forma um triângulo.")
else:
    print("Não forma um triângulo.")
