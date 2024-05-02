varIMC      =   ...; #PlaceHolder / Espaço vazio / none.
varAltura   =   float(input('Insira sua altura em metros: '));
varPeso     =   int(input('Insira seu peso: '));
varIMC      =   (varPeso / (varAltura ** 2));

print(f'Seu IMC é igual a {varIMC:.2f}');