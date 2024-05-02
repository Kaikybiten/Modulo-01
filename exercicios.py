"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
varNumber = input();

if (varNumber.isdigit()): #Verifica se a string só possui números
    varNumber = int(varNumber);
    if (varNumber & 1):
        print(f'{varNumber} é um número impar');
    else:
        print(f'{varNumber} é um número par');
else:
    print(f'"{varNumber}" não é um número inteiro');

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
varTime = int(input('Que horas são?'));

if (varTime >= 0 and varTime <= 11):
    print('BOM DIA!');
elif (varTime <= 18):
    print('BOA TARDE');
elif (varTime <= 23):
    print('BOA NOITE!');

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
varName = input('Insira seu nome: ');

if (len(varName) <= 4):
    print('Seu nome é curto');
elif (len(varName) <= 6):
    print('Seu nome é normal');
elif (len(varName) <= 6):
    print('Seu nome é muito grande');