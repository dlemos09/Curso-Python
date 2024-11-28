#Métodos
# Cadastro email: naruto@gmail.com senha: kurama1234

class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.enderecos = ['Rua 1', 'Rua 2']
    
    # permite uma string a partir de uma classe
    def __str__(self):
        return f'email: {self.email}, senha: {self.senha}'
    
    #utilizado para percorrer algo do usuário
    def __iter__(self):
       return self.enderecos.__iter__()
        
    #inserir o _ mostra que o método é privado!
    def _validar(self):
        email_cadastro = 'naruto@gmail.com'
        senha_cadastro = 'kurama1234'
        
        if email_cadastro == self.email and senha_cadastro == self.senha:
            print('Usuário validado')
        else:
            print('Usuário inválido')
    
    def logar(self):
        self._validar()
        print('Envia para tela principal')
    #    pass
    
    def forca_senha(self):
        if len(self.senha) >= 5:
            return True
        else:
            return False
    
    # def cadastrar_endereco(self, endereco1, endereco2):
    #     print(f'Endereços: {endereco1}, {endereco2}')
        
    def cadastrar_endereco(self, *enderecos):
        for endereco in enderecos:
            print(f'endereço: {endereco}')
                
usuario = Usuario('naruto@gmail.com', 'kurama1234')
usuario.enderecos = ['Rua 1', 'Rua 2', 'Rua 3']

# for endereco in usuario.enderecos:
#     print(f'Endereço: {endereco}')
    
for endereco in usuario:
     print(f'Endereço: {endereco}')
    
print(usuario)
# usuario.logar()

# if usuario.forca_senha():
#     print('Senha Forte')
# else:
#     print('Senha Fraca')

# usuario.cadastrar_endereco('Rua 1', 'Rua 2')

#lista = ['Rua 1', 'Rua 2']
#usuario.cadastrar_endereco(*lista) # O  '*' faz o "unpack", distribui o primeiro item da lista para o primeiro parametro.
# usuario.cadastrar_endereco('Rua 1', 'Rua 2')


