

#Polimorfismo -> Qualidade ou estado de ser capaz de assumir diferentes formas

# Poli -> Muitas
# morfo -> formas

class Animal: #SuperClasse, classe pai
     def __init__(self):
        self.cor=''
        self.tamanho=''
        self.peso=''
        
     def correr(self):
        print('correr como um ')
            
     def dormir(self):
        print('dormir')
        
class Cao(Animal): #subclasse, classe filha
     def latir(self):
        print('latir')
    # sobreescrita de método -> override
     def correr(self):
        super().correr()
        print('cao')

class Ave(Animal): #subclasse, classe filha
     def voar(self):
         print('voar')
    # sobreescrita de método -> override
     def correr(self):
        super().correr()
        print('ave')


# cao = Cao()
# cao.correr()

ave = Ave()
ave.correr()