# Descrição: Crie um sistema para gerenciar uma biblioteca. Deve ser possível adicionar livros, emprestar livros e consultar os livros disponíveis.

class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista para armazenar os livros

    def adicionar_livro(self, titulo):
        self.livros.append(titulo)
        print(f"Livro '{titulo}' adicionado com sucesso!")

    def emprestar_livro(self, titulo):
        if titulo in self.livros:
            self.livros.remove(titulo)
            print(f"Você emprestou o livro '{titulo}'.")
        else:
            print(f"O livro '{titulo}' não está disponível.")

    def listar_livros(self):
        if self.livros:
            print("Livros disponíveis:")
            for livro in self.livros:
                print(f"- {livro}")
        else:
            print("Nenhum livro disponível.")

# Testando o sistema
biblioteca = Biblioteca()
biblioteca.adicionar_livro("Python para Iniciantes")
biblioteca.adicionar_livro("Aprendendo Java")
biblioteca.listar_livros()
biblioteca.emprestar_livro("Python para Iniciantes")
biblioteca.listar_livros()
