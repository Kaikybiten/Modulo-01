varNames = []


while (True):
    varNames.append(input('Insira um nome à lista, caso deseja parar de inserir nomes digite "stop": ').capitalize())
    
    if ("Stop" in varNames):
        varNames.pop()
        break

varIndice = range(len(varNames))

print('\nNomes digitados:')
for indice in varIndice:
    print(indice, varNames[indice], sep=' - ' )

# OU...

for name in enumerate(varNames):
    #Estilizando...
    indice, nome = name
    print(indice, nome, sep=' - ' )

# OU... 

for indice, nome in enumerate(varNames):
    #Estilizando...
    print(indice, nome, sep=' - ' )