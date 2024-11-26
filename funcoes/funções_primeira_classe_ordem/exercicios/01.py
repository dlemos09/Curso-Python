# Função de saudação
def saudacao(nome):
    return f"Olá, {nome}!"

# Função que recebe outra função como argumento
def imprimir_mensagem(funcao, argumento):
    print(funcao(argumento))

# Testando
imprimir_mensagem(saudacao, "Maria")  # Saída: Olá, Maria!
