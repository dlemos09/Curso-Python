# Funções simples
def adicionar(x):
    return x + 5

def multiplicar(x):
    return x * 3

# Função que compõe duas funções
def compor(fun1, fun2, valor):
    return fun2(fun1(valor))

# Testando
print(compor(adicionar, multiplicar, 2))  # Saída: 21
