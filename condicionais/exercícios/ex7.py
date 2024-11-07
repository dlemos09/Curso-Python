# Calcula o valor final de um produto com desconto progressivo.
valor = float(input("Digite o valor do produto: R$ "))

if valor > 100:
    desconto = valor * 0.10
    valor_final = valor - desconto
    print("Desconto de 10% aplicado.")
elif 50 <= valor <= 100:
    desconto = valor * 0.05
    valor_final = valor - desconto
    print("Desconto de 5% aplicado.")
else:
    desconto = valor * 0.02
    valor_final = valor - desconto
    print("Desconto de 2% aplicado.")

print("Valor final: R$ {:.2f}".format(valor_final))
