varString = 'eu me chamo {0} e moro no {1}, eu amo meu país, aqui no {1} jogamos {2}, ao contrario da maioria do {1}, eu, {0}, não gosto de {2}.';

varNome     = 'Kaiky';
varPaís     = 'Brasil';
varFutebol  = 'futebol';

print(varString.format(varNome, varPaís, varFutebol));

#Intepolação
varDinheiro = float(10.00);
print('%s tem R$%.2f' % (varNome, varDinheiro));

print("%i em hexadecimal é %04X" % (45, 45)); #O NUMERO SERA CONVERTIDO PARA HEXADECIMAL.

#Adicionando caracteres
print(f'{varPaís:->10}') #A ESQUERDA, MANTENDO O TEXTO A DIREITA ">"
print(f'{varPaís:-<10}') #A DIREITA, MANTENDO O TEXTO A ESQUERDA "<"
print(f'{varPaís:-^10}') #A AMBOS OS LADOS, MANTENDO O TEXTO NO CENTRO "^"