# Função que retorna uma função de cálculo de imposto
def calcular_imposto(taxa):
    return lambda valor: valor * (1 + taxa)

# Criando uma função com taxa de 10%
imposto_10 = calcular_imposto(0.10)
print(imposto_10(100))  # Saída: 110.0
