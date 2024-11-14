# Criando Dicionários em Python
# Dicionários podem ser criados usando chaves {} ou a função dict().


# Criando um dicionário com chaves
pessoa = {
    "nome": "João",
    "idade": 30,
    "altura": 1.76,
    "endereco": {
        "cidade": "São Paulo",
        "rua": 'Saída: Rua das Flores'
    } 
}

# Ou usando a função dict()
pessoa = dict(nome="João", idade=30, cidade="São Paulo")

# Acessando Elementos no Dicionário
# Para acessar valores em um dicionário, basta usar a chave entre colchetes [].

print(pessoa["nome"])  # Saída: João
print(pessoa["idade"]) # Saída: 30
print(pessoa['endereco']['rua'])  # Saída: Rua das Flores

# É possível também usar o método get() para acessar uma chave. Se a chave não existir, get() retorna None (ou um valor padrão que você pode definir), evitando um erro.

print(pessoa.get("cidade", "Cidade não encontrada"))  # Saída: São Paulo
print(pessoa.get("profissao", "Profissão não encontrada"))  # Saída: Profissão não encontrada


# Modificando Elementos no Dicionário
# Você pode modificar o valor de uma chave existente ou adicionar novos pares chave-valor.

# Alterando o valor de uma chave
pessoa["idade"] = 31

# Adicionando um novo par chave-valor
pessoa["profissao"] = "Engenheiro"


# Removendo Elementos do Dicionário
# O Python oferece várias formas de remover itens de um dicionário:

# pop(): Remove um item específico, referenciado pela chave, e retorna o valor removido.

idade = pessoa.pop("idade")
print(idade)  # Saída: 31

# del: Remove um item específico usando a palavra-chave del.

del pessoa["cidade"]

# clear(): Remove todos os itens do dicionário.

pessoa.clear()

# Operações e Métodos Úteis dos Dicionários
# Dicionários possuem métodos úteis que ajudam na manipulação de dados.

# keys(): Retorna todas as chaves do dicionário.

print(pessoa.keys())  # Saída: dict_keys(['nome', 'profissao'])


# values(): Retorna todos os valores do dicionário.

print(pessoa.values())  # Saída: dict_values(['João', 'Engenheiro'])

# items(): Retorna pares chave-valor do dicionário como tuplas.

print(pessoa.items())  # Saída: dict_items([('nome', 'João'), ('profissao', 'Engenheiro')])

# update(): Atualiza o dicionário com pares chave-valor de outro dicionário.

pessoa.update({"nome": "Carlos", "idade": 32})


# Exemplo de Uso: Contagem de Palavras
# Dicionários são muito usados para contar ocorrências, associar informações e agrupar dados. Aqui vai um exemplo de contagem de palavras em uma frase.

# Frase de exemplo
frase = "Python é simples e poderoso e simples é Python"

# Inicializa um dicionário para contagem
contagem_palavras = {}

# Divide a frase em palavras e conta cada uma
for palavra in frase.split():
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

print(contagem_palavras)
# Saída: {'Python': 2, 'é': 2, 'simples': 2, 'e': 2, 'poderoso': 1}



