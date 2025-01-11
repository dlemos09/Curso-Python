
# Encapsulamento

#Esconder detalhes da implementação, dando mais segurança a sua aplicação. O Encapsulamento serve para controlar o acesso aos atributos e métodos de uma classe.


# class Filtro:
#     def __init__(self, imagem):
#         self.imagem = imagem
        
#     def preto_e_branco(self):
#         print(f'{self.imagem} com filtro preto e branco')
    
#     def foto_envelhecida(self):
#         print(f'{self.imagem} com filtro envelhecido')
#         print(f'também com efeito amarelado')
        
# filtro = Filtro('foto_naruto')
# filtro.preto_e_branco()
# filtro.foto_envelhecida()

# Controle de acesso Getter e Setters

class Conta:
    # def __init__(self, numero, saldo): #construtor
    def __init__(self, saldo): #construtor
        # self._numero = numero
        self._numero = 0
        self._saldo = saldo
        
    def depositar(self, valor):
        self._saldo += valor
        
    def get_numero(self):
        return self._numero
    
    def get_numero(self,valor):
         self._numero = valor
        
    def sacar(self, valor):
        self._saldo -= valor
        
# conta = Conta(10232, 900)
conta = Conta(900)

conta.set_numero(10232)
print(conta.get_numero())
# conta.sacar(100)
# conta.depositar(50)
# conta.saldo = 0
# print(conta._saldo)
