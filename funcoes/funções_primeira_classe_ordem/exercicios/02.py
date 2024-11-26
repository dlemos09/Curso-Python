# Função de ordem superior
def aplicar_a_lista(funcao, lista):
    return [funcao(item) for item in lista]

# Função simples para multiplicar por 2
def dobrar(x):
    return x * 2

# Testando
numeros = [1, 2, 3, 4]
print(aplicar_a_lista(dobrar, numeros))  # Saída: [2, 4, 6, 8]
