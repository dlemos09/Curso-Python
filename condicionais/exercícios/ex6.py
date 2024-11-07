# Converte uma nota numérica em um conceito de A a F.
nota = float(input("Digite a nota (0 a 100): "))

if 90 <= nota <= 100:
    conceito = "A"
elif 80 <= nota < 90:
    conceito = "B"
elif 70 <= nota < 80:
    conceito = "C"
elif 60 <= nota < 70:
    conceito = "D"
elif 0 <= nota < 60:
    conceito = "F"
else:
    conceito = None
    print("Nota inválida.")

if conceito:
    print("Conceito:", conceito)
