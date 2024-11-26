# Função como objeto
def saudacao(nome):
    return f"Olá, {nome}!"

# Atribuindo a uma variável
cumprimentar = saudacao
print(cumprimentar("Maria"))  # Saída: Olá, Maria!


# Função de ordem superior

def aplicar_operacao(funcao, a, b):
    return funcao(a, b)

# Definindo funções simples
def soma(x, y):
    return x + y

def multiplicacao(x, y):
    return x * y

# Usando a função de ordem superior
print(aplicar_operacao(soma, 3, 4))        # Saída: 7
print(aplicar_operacao(multiplicacao, 3, 4))  # Saída: 12
