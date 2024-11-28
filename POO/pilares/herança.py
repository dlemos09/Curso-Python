#Herança

# class Cao:
#     def __init__(self):
#         self.cor=''
#         self.tamanho=''
#         self.peso=''
        
#     def correr(self):
#         print('correr')
            
#     def dormir(self):
#         print('dormir')
        
#     def latir(self):
#         print('latir')
        
# class Ave:
#     def __init__(self):
#         self.cor=''
#         self.tamanho=''
#         self.peso=''
        
#     def correr(self):
#         print('correr')
            
#     def dormir(self):
#         print('dormir')
        
#     def voar(self):
#         print('voar')

# cao = Cao()
# cao.cor = 'Marrom'
# cao.correr()
# print(cao.cor)

# ave = Ave()
# ave.cor = 'Preto'
# ave.correr()
# ave.voar()
# print(ave.cor)

class Animal: #SuperClasse, classe pai
     def __init__(self):
        self.cor=''
        self.tamanho=''
        self.peso=''
        
     def correr(self):
        print('correr')
            
     def dormir(self):
        print('dormir')
        
class Cao(Animal): #subclasse, classe filha
     def latir(self):
        print('latir')

class Ave(Animal): #subclasse, classe filha
     def voar(self):
         print('voar')
         
         

cao = Cao()
cao.cor = 'Marrom'
cao.correr()
cao.latir()
print(cao.cor)

ave = Ave()
ave.cor = 'Preto'
ave.correr()
ave.voar()
print(ave.cor)
