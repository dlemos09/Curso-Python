# Solicita uma nota e classifica como "Reprovado", "Recuperação" ou "Aprovado".
nota = float(input("Digite a nota: "))
if nota >= 7.0:
    print("Aprovado")
elif 5.0 <= nota < 7.0:
    print("Recuperação")
else:
    print("Reprovado")
