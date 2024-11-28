

class Conta:
    def __init__(self, nome, saldo): #construtor
        self.nome = nome
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        self.saldo -= valor
        
    
 
conta = Conta("Douglas", 1000) # -> instaciar um objeto
# conta.depositar(100)
# print(conta.nome)
conta.sacar(100)
print(f'nome: {conta.nome} - saldo: R${conta.saldo}')

 
conta = Conta("Maria", 1800) # -> instaciar um objeto
conta.depositar(900)
conta.sacar(100)
print(f'nome: {conta.nome} - saldo: R${conta.saldo}')