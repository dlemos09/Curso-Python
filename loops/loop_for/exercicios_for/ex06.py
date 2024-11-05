# Multiplica dois vetores de 2x2 e imprime o resultado.
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
resultado = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            resultado[i][j] += matriz1[i][k] * matriz2[k][j]
print("Resultado da multiplicação:", resultado)
