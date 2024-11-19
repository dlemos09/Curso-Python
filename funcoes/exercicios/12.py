# 12. Palíndromo

def eh_palindromo(texto):
    # Verifica se a string é um palíndromo
    texto = texto.replace(" ", "").lower()  # Remove espaços e converte para minúsculas
    return texto == texto[::-1]

# Testando a função
print(eh_palindromo("arara"))  # Saída: True
print(eh_palindromo("Python"))  # Saída: False
