# Introdução às Funções em Python

# As funções em Python são blocos de código reutilizáveis que executam uma tarefa específica. Elas permitem que você organize seu programa, evite a repetição de código e aumente a legibilidade. Funções podem receber entradas (parâmetros) e retornar saídas (valores).

# Tipos de Funções em Python
# 1. Funções Internas (Built-in Functions)
# São funções já incluídas no Python, como print(), len(), max(), etc.

# Usando a função interna len() para obter o tamanho de uma lista
lista = [1, 2, 3, 4]
print(len(lista))  # Saída: 4


# 2. Funções Definidas pelo Usuário
# Criadas pelo programador para realizar tarefas específicas. São definidas com a palavra-chave def.

# Exemplo:
    
def saudacao(nome):
    # Função que imprime uma saudação personalizada
         print(f"Olá, {nome}!")
saudacao("Maria")  # Saída: Olá, Maria!

# 3. Funções com Retorno
# Essas funções devolvem um valor com a palavra-chave return.

def soma(a, b):
    # Retorna a soma de dois números
    return a + b

resultado = soma(3, 4)
print(resultado)  # Saída: 7


# 4. Funções Lambda
# São funções anônimas, geralmente usadas para operações rápidas e simples. Definidas com a palavra-chave lambda.

# Exemplo

# Função lambda para multiplicar dois números
multiplicar = lambda x, y: x * y
print(multiplicar(3, 5))  # Saída: 15


# 5. Funções com Parâmetros Padrão
# Permitem valores padrão para os parâmetros, caso não sejam fornecidos.

# Exemplo:
    
def mensagem(texto="Olá!"):
    # Imprime uma mensagem com valor padrão
    print(texto)
    
mensagem()            # Saída: Olá!
mensagem("Bem-vindo")  # Saída: Bem-vindo

# 6. Funções com Argumentos Arbitrários
# Permitem receber uma quantidade variável de argumentos com *args (tuplas) ou **kwargs (dicionários).

def soma_todos(*numeros):
    # Soma todos os números fornecidos
    return sum(numeros)

print(soma_todos(1, 2, 3, 4))  # Saída: 10

def dados_pessoais(**kwargs):
    # Exibe as informações fornecidas como dicionário
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

dados_pessoais(nome="João", idade=30, cidade="São Paulo")
# Saída:
# nome: João
# idade: 30
# cidade: São Paulo



#Calculo média

nome = (input('Digite seu nome: '))

def calcular_media(nota1, nota2, nota3):
    soma = nota1 + nota2 + nota3
    media = soma/3
    return media

retorno = calcular_media(
    nota1 = float(input('Digite a primeira nota1: ')),
    nota2 = float(input('Digite a primeira nota2: ')),
    nota3 = float(input('Digite a primeira nota3: '))
)

if retorno >= 7.0:
    print(f'{nome} está aprovado, sua media foi {retorno}')
elif 5.0 <= retorno <= 7.0:
    (f'{nome} está recuperação, sua media foi {retorno}')
else:
    (f'{nome} está reprovado, sua media foi {retorno}')