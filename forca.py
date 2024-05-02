import os

varPalavraSecreta = 'filosofia';
varLetrasAcertadas = "";
varTentativas = 0;

while (True):
    
    varPalavraFormada = "";

    varLetra = input(f'A palavra secreta possui {len(varPalavraSecreta)} letra, Tente adivinha-la, chutando uma letra: ');

    if(len(varLetra) != 1):
        print('Insira apenas 1 letra');
        continue;
    
    varTentativas += 1;

    varLetra = varLetra.lower(); #Deixando a letra digitada em minuscula.

    if (varLetra in varPalavraSecreta):
        varLetrasAcertadas += varLetra;
    else:
        print('Está letra não está na plavra');
        print(varPalavraFormada);
        continue;

    for letra in varPalavraSecreta:
        if (letra in varLetrasAcertadas):
            varPalavraFormada += letra;
        else:
            varPalavraFormada += "*";

    print(varPalavraFormada);

    if (varPalavraFormada == varPalavraSecreta):
        os.system("cls");
        print(f'MEUS PARABÉNS VOCÊ ENCONTROU A PALAVRA');
        print(f'A palavra secreta era "{varPalavraSecreta}"');
        
        varContinuar = input("Deseja jogar novamente? (s/n): ")
        if (varContinuar.lower() == 'n'):
            break;

        varLetrasAcertadas = "";
        varTentativas = 0;