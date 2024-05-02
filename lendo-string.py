varNome = input('Digite seu nome ');
varIdade = input('Digite sua idade ');

if ((varNome) and (varIdade)):
    print(f'Seu nome é {varNome}');
    print(f'Seu nome invertido é {varNome[::-1]}'); #[inicio:fim:passos] nesse caso os passo estão indo ao contrario (-1 letra por vez).
    if (' ' in varNome):
        print('Seu nome contém espaços');
    else:
        print('Seu nome não contém espaços');
    print(f'Seu nome contém {len(varNome)} letras');
    print(f'A primeira letra do seu nome é {varNome[0]}');
    print(f'A ultima letra do seu nome é {varNome[len(varNome) - 1]}');
else:
    print('Desculpe, você deixou campos vazios.');