varLista = [10, 20, 30] #Cria uma lista
print(varLista)

varLista.append(50) #Adiciona um item ao final da lista
print(varLista)

varLista[3] = 40 #Modifica o item pertecente ao index [3]
print(varLista)

del varLista[0] #Deleta o item pertecente ao index [0]
print(varLista)
print(varLista[0]) #Mostra o atual item que passou a pertecer ao index [0]

varDeletado = varLista.pop() #Deleta o ultimo item da lista (nesse caso ele foi armazenado na variavel)
print(varLista)
print(varDeletado) #Mostra o valor que foi deletado

varLista.insert(0, -10) #Adiciona um item ao index indicado
print(varLista)

varLista01 = [40, 50, 60]
varLista.extend(varLista01) #Adiciona os itens de uma lista para outra
print(varLista)

varLista02 = [-60, -50, -40]
print(varLista02 + varLista01) #Concatenar os itens de amabas as listas

varLista.clear() #Limpa a lista totalmente
print(varLista)

# Ordenando os valores da lista
varLista03 = [7, 5, 2, 8, 0, 1, 4]
sorted(varLista03)
print(varLista03)