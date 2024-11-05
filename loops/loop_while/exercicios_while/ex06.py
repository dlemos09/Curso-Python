# Pede a senha até que a senha correta seja digitada.
senha = "1234"
tentativa = input("Digite a senha: ")
while tentativa != senha:
    tentativa = input("Senha incorreta. Tente novamente: ")
print("Acesso permitido")
