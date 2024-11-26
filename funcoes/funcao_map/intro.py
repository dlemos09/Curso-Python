# Função map
# A função map aplica uma função a cada elemento de um iterável e retorna um novo iterável.

# Sintaxe: 
    
#     map(funcao, iteravel)


# Multiplicando cada número por 2
numeros = [1, 2, 3, 4]
resultado = map(lambda x: x * 2, numeros)
print(list(resultado))  # Saída: [2, 4, 6, 8]
