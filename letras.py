varNome = 'kaiky';

for i in range (5):
    print(varNome[i]);

if ('a' in varNome):
    print(f'a letra "a" esta na string {varNome}');
else:
    print(f'a letra "a" não esta na string{varNome}');

print(100* '-');

if ('e' not in varNome):
    print(f'a letra "e" não esta na string {varNome}');
else:
    print(f'a letra "e" esta na string{varNome}');