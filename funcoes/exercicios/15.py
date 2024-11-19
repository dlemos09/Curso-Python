# 15. Validação de Senha

import re

# O comando import re é utilizado em Python para importar o módulo re, que é o módulo de expressões regulares (Regular Expressions). Este módulo fornece ferramentas para trabalhar com padrões de texto, como busca, substituição, e validação de strings de acordo com regras específicas.

def validar_senha(senha):
    # Valida uma senha com os critérios fornecidos
    if len(senha) < 8:
        return "Senha deve ter pelo menos 8 caracteres."
    if not re.search(r"[A-Z]", senha):
        return "Senha deve conter pelo menos uma letra maiúscula."
    if not re.search(r"[0-9]", senha):
        return "Senha deve conter pelo menos um número."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return "Senha deve conter pelo menos um caractere especial."
    return "Senha válida!"

# Testando a função
print(validar_senha("Senha123!"))  # Saída: Senha válida!
print(validar_senha("senha123"))   # Saída: Senha deve conter pelo menos uma letra maiúscula.
