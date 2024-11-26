# Definindo algumas funções simples para operações matemáticas
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:  # Evita divisão por zero
        return x / y
    return "Divisão por zero não permitida."

# Função de ordem superior que aplica uma operação
def aplicar_operacao(funcao, a, b):
    return funcao(a, b)

# Testando as operações
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Escolha da operação
operacao = input("Escolha a operação (somar, subtrair, multiplicar, dividir): ").strip().lower()

# Dicionário para associar strings às funções
operacoes = {
    "somar": somar,
    "subtrair": subtrair,
    "multiplicar": multiplicar,
    "dividir": dividir
}

# Verifica se a operação é válida e aplica
if operacao in operacoes:
    resultado = aplicar_operacao(operacoes[operacao], num1, num2)
    print(f"Resultado: {resultado}")
else:
    print("Operação inválida.")
