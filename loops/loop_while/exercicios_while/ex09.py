# Jogo onde o usuário tenta adivinhar um número secreto.
import random
numero_secreto = random.randint(1, 100)
tentativa = int(input("Adivinhe o número (1-100): "))
while tentativa != numero_secreto:
    if tentativa < numero_secreto:
        print("Muito baixo.")
    else:
        print("Muito alto.")
    tentativa = int(input("Tente novamente: "))
print("Parabéns! Você acertou.")
