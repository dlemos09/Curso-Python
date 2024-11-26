# Objetivo: Calcular o produto de todos os números em uma lista utilizando reduce.


from functools import reduce

# Lista de números
numeros = [2, 3, 4]

# Usando reduce para calcular o produto dos números
produto = reduce(lambda x, y: x * y, numeros)

# Exibe o resultado
print(produto)  # Saída: 24


# A função reduce aplica a função lambda (que multiplica dois números) aos elementos da lista numeros.

# Inicialmente, ela começa multiplicando os dois primeiros elementos (2 * 3), depois o resultado da multiplicação é multiplicado pelo próximo número (6 * 4), até que todos os elementos da lista sejam processados.

# O resultado final é 24.