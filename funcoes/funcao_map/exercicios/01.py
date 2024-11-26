# Conversão usando map
temperaturas = [0, 20, 30, 40]
f_temperaturas = list(map(lambda c: (c * 9/5) + 32, temperaturas))
print(f_temperaturas)  # Saída: [32.0, 68.0, 86.0, 104.0]
