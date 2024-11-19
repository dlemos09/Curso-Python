numbers = [10, 5, 7, 2, 1]
print("Conteúdo da lista original:", numbers) # Imprimindo o conteúdo da lista original.

numbers[0] = 111

print ("\nConteúdo da lista anterior:", numbers) # Imprimindo conteúdo da lista anterior.

numbers[1] = numbers [4] # Copiando o valor do quinto elemento para o segundo.
print("Conteúdo da lista anterior:", numbers) # Imprimir o conteúdo da lista anterior.

print ("\n List length:", len (numbers)) # Imprimindo o comprimento da lista.

del numbers[1] # Removendo o segundo elemento da lista.
print ("Comprimento da nova lista:", len (numbers)) # Imprimindo novo comprimento da lista.
print ("\nNova lista de conteúdo:", numbers) # Imprimindo conteúdo da lista atual.

### Essa operação é realizada por um método chamado append(). Ele pega o valor do argumento e o coloca no final da lista que possui o método.

numbers.append (4)


print(len(numbers))

print(numbers)

### O método insert() é um pouco mais inteligente - ele pode adicionar um novo elemento em qualquer lugar na lista, não apenas no final.

numbers.insert (0, 222)

print(len (numbers))
print(numbers)


 # São necessários dois argumentos:

###o primeiro mostra a localização necessária do elemento a ser inserido; Nota: todos os elementos existentes que ocupam locais à direita do novo elemento (inclusive o na posição indicada) são deslocados para a direita, a fim de liberar espaço para o novo elemento;
###o segundo é o elemento a ser inserido.


# Se preferir, você pode combinar o novo elemento com a lista existente usando o operador de desempacotamento *.


# Lista original
minha_lista = [2, 3, 4, 5]

# Cria uma nova lista com o elemento no início
minha_lista = [1, *minha_lista]

print(minha_lista)  # Saída: [1, 2, 3, 4, 5]


