import os

varCompras = []

def exibir_lista():
    for indice, item in enumerate(varCompras):
        print(indice, item, sep=' - ')

while True:
    varMenu = input('Oque deseja fazer?\n1 - Inserir produto à lista\n2 - Apagar item da lista\n3 - Listar produtos digitados\n')

    if (varMenu == '1'):
        os.system('cls')
        print('Qual item deseja adicionar? digite "stop" para parar de inserir produtos:\n')
        while ('stop' not in varCompras):
            varCompras.append(input())
        varCompras.pop()
    elif (varMenu == '2'):
        os.system('cls')
        exibir_lista()
        varDeleteStr = input('Qual item deseja deletar? ')
        try:
            varDeleteInt = int(varDeleteStr)
            varCompras.pop(varDeleteInt)
        except ValueError:
            print('Insira um numero inteiro')
        except IndexError:
            print('A lista não possui esse indice')
    elif (varMenu == '3'):
        os.system('cls')
        exibir_lista()
    else:
        print('Opção invalida');