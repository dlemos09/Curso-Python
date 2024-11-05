"""
Estruturas condicionais
if  (se)
else (senao)

condicao = idade >= 18 #verdadeira
# criança, adolescente e adulto
"""
idade = int(input('Digite sua idade: '))

if idade <=13:
    print("criança")
elif idade <= 18:
    print("adolescente")
elif idade <= 30:
    print("adulto 1")
else:
    print("adulto 2")


"""
Operadores ternário
"""
# idade = 20
# #resultado = ('Menor idade','Maior idade')[idade>=18]
# resultado = 'Maior idade' if idade>=18 else 'Menor idade'
# print(resultado)


