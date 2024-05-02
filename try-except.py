varNumber = input('Insira qualquer numero: ');

try: #Caso ocorra um erro nesse trecho, o programa irá pular para o trecho "except"
    varNumber = float(varNumber);
    print(f'O dobro de {varNumber:.2f} é {varNumber * 2}');
except:
    print(f'"{varNumber}" Não é um número');