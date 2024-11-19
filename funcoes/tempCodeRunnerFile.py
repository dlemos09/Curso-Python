alunos = [
    {'nome': 'Jamilton', 'notas': [8, 8]},
    {'nome': 'Ana', 'notas': [10, 9, 10]},
    {'nome': 'Maria', 'notas': [10, 10, 10, 8]},
]


def calcular_media(notas):
    totalNotas = 0
    for nota in notas:
        totalNotas += nota
    media = totalNotas / len(notas)
    return media

for aluno in alunos:
    nome = aluno['nome']
    notas = aluno['notas']
    media = calcular_media(notas)
    print(f'Média do(a) {nome} é {media}')
