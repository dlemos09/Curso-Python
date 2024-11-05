# Converte uma tupla para lista, modifica e reconverte para tupla.
tupla = (10, 20, 30, 40)
lista = list(tupla)
lista[0] = 100  # Modifica o primeiro elemento
tupla_modificada = tuple(lista)
print("Tupla modificada:", tupla_modificada)
