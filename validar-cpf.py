while (True):
    varCPF = input('Insira seu CPF, apenas números, sem pontos ou traços:')

    if (len(varCPF) != 11):
        print('Insira um CPF valido!')
        continue
    if (not(varCPF.isdigit())):
        print('Insira apenas numeros!')
        continue

    varSequencia = varCPF == varCPF[0] * len(varCPF)
    if (varSequencia):
        print('Não envie dados sequenciais')
        continue

    varSoma = 0
    varMultiplos = 10
    for i in range(9):
        num = int(varCPF[i])
        varSoma += varMultiplos * num
        varMultiplos -= 1

    varNumero01 = (10 * varSoma) % 11
    varNumero01 = varNumero01 if varNumero01 <= 9 else 0

    varSoma = 0
    varMultiplos = 11
    for i in range(10):
        num = int(varCPF[i])
        varSoma += varMultiplos * num
        varMultiplos -= 1

    varNumero02 = (10 * varSoma) % 11
    varNumero02 = varNumero02 if varNumero02 <= 9 else 0

    varCpfGerado = f'{varCPF[:9]}{varNumero01}{varNumero02}'

    if (varCpfGerado == varCPF):
        print('CPF valido!')
    else:
        print('CPF invalido!')