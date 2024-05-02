varLista00 = [10, 20, 30, 40]
varLista01 = varLista00 #Criando uma variavel e fazendo ela receber o valor da lista 00        

print('lista00: ', varLista00)
print('lista01: ', varLista01)

varLista00[2] = 'Este item foi alterado' #Neste caso as duas listas estão armazenadas no mesmo local de memoria, ou seja, tudo que for alterado em uma, será na outra

print('lista00: ', varLista00)
print('lista01: ', varLista01)



varLista00 = [10, 20, 30, 40]
varLista01 = varLista00.copy() #Criando uma variavel e copiando os valores da lista 00 para ela

print('lista00: ', varLista00)
print('lista01: ', varLista01)

varLista00[2] = 'Este item foi alterado' #Já neste caso as listas estão armazenadas em locais de memoria distintos, ou seja, modificar uma, não modifica a outra

print('lista00: ', varLista00)
print('lista01: ', varLista01)