# 1º Abstração

# É o processo de entender objetos do mundo real e implementar isso em programação.

# class Carro:
#     def __init__(self, motor, ano):
#         self.motor = motor


class Carro:
    def __init__(self, modelo, cor, placa):
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        
    def exibir_local_atual(self):
        print('Carro está no Beco Diagonal')

#MODELO
carro = Carro() # Quando se instacia, você passa a ter uma entidade;

carro_douglas = Carro('Fusca', 'Azul', 'DAR-1234') # Na instancia você pode identificar, logo você tem identidade.

carro_natanael = Carro('Gol', 'Prata', 'BRR-0134')

# Outro exemplo

class Produto:
    #roupas
    def __init__(self, tamanho, cor, preco):
        self.tamanho = tamanho
        self.cor = cor
        self.preco = preco
        
produto = Produto('M', 'Preto', '25.90')


class ProtutoEletronico:
    def __init__(self, largura, altura, cor, preco):
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.preco = preco
        
produto2 = Produto('50cm', "80cm", 'Preto', '1800')
