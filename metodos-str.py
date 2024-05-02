varTexto = 'Olá, querido papai noel.'

varSeparado = varTexto.split(',')
print(varSeparado)

for i, f in enumerate(varSeparado):
    print(varSeparado[i])

for i, f in enumerate(varSeparado):
    print(varSeparado[i].strip())

varNumeros = '123456789'
print('-'.join(varNumeros))