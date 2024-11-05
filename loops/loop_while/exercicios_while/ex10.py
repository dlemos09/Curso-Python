# Calcula e imprime a sequência de Fibonacci até o n-ésimo termo.
n = int(input("Quantos termos da sequência de Fibonacci deseja ver? "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
