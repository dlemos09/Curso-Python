# 5. Tabuada

num = int(input('Digite um número'))

while num < 1 or num > 10:
    num = int(input('Digite um número entre 1 e 10'))
    

def tabuada(numero):
    numero = num
    # Imprime a tabuada do número fornecido
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Testando a função
tabuada(num)
