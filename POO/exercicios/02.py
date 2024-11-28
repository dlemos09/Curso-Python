# Descrição: Crie um sistema para gerenciar informações de estudantes em uma escola. O sistema deve permitir:

# Adicionar estudantes com nome, idade e matrícula.
# Exibir informações de todos os estudantes.
# Buscar um estudante pelo número de matrícula.
# Remover um estudante pela matrícula.

class Estudante:
    """
    Classe que representa um estudante.
    """
    def __init__(self, nome, idade, matricula):
        self.nome = nome  # Nome do estudante
        self.idade = idade  # Idade do estudante
        self.matricula = matricula  # Número de matrícula

    def exibir_informacoes(self):
        """
        Exibe as informações do estudante.
        """
        print(f"Matrícula: {self.matricula} | Nome: {self.nome} | Idade: {self.idade}")


class SistemaEscolar:
    """
    Classe para gerenciar o sistema escolar.
    """
    def __init__(self):
        self.estudantes = []  # Lista para armazenar estudantes

    def adicionar_estudante(self, nome, idade, matricula):
        """
        Adiciona um novo estudante ao sistema.
        """
        # Verifica se a matrícula já existe
        for estudante in self.estudantes:
            if estudante.matricula == matricula:
                print("Erro: Matrícula já existente!")
                return

        # Cria um novo objeto Estudante e adiciona à lista
        novo_estudante = Estudante(nome, idade, matricula)
        self.estudantes.append(novo_estudante)
        print(f"Estudante '{nome}' adicionado com sucesso!")

    def exibir_estudantes(self):
        """
        Exibe todos os estudantes cadastrados.
        """
        if not self.estudantes:
            print("Nenhum estudante cadastrado.")
        else:
            print("\n--- Lista de Estudantes ---")
            for estudante in self.estudantes:
                estudante.exibir_informacoes()

    def buscar_estudante(self, matricula):
        """
        Busca um estudante pelo número de matrícula.
        """
        for estudante in self.estudantes:
            if estudante.matricula == matricula:
                print("\n--- Estudante Encontrado ---")
                estudante.exibir_informacoes()
                return
        print("Erro: Estudante não encontrado.")

    def remover_estudante(self, matricula):
        """
        Remove um estudante pelo número de matrícula.
        """
        for estudante in self.estudantes:
            if estudante.matricula == matricula:
                self.estudantes.remove(estudante)
                print(f"Estudante com matrícula {matricula} removido com sucesso!")
                return
        print("Erro: Matrícula não encontrada.")


# Testando o sistema
sistema = SistemaEscolar()

# Adicionando estudantes
sistema.adicionar_estudante("Alice", 20, "2024001")
sistema.adicionar_estudante("Bob", 22, "2024002")
sistema.adicionar_estudante("Carol", 19, "2024003")

# Exibindo estudantes
sistema.exibir_estudantes()

# Buscando um estudante
sistema.buscar_estudante("2024002")

# Removendo um estudante
sistema.remover_estudante("2024001")

# Exibindo novamente após remoção
sistema.exibir_estudantes()
