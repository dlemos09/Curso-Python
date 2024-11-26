# Funções simples
def dobrar(x):
    return x * 2

def subtrair_1(x):
    return x - 1

# Função de ordem superior que aplica múltiplas funções
def aplicar_funcoes(lista, funcoes):
    return [[func(x) for func in funcoes] for x in lista]

# Testando
numeros = [1, 2, 3]
funcoes = [dobrar, subtrair_1]
print(aplicar_funcoes(numeros, funcoes))  # Saída: [[2, 0], [4, 1], [6, 2]]
