varTexto = 'O cristianismo se converteu num culto a um Jesus abstrato, mítico, dissociado da sua ação concreta e histórica, dissociado, inclusive da própria Bíblia. Enquanto choram abraçando uma figura que o representa, repelem e se afastam do miserável, do preso, do discriminado, da justiça.';

print(varTexto);
i = 0;
varLetraAnterior = varTexto[i];

while(i < len(varTexto)):

    varLetraAtual = varTexto[i];

    i +=1;

    if (varLetraAtual == " "):
        continue

    if (varTexto.count(varLetraAtual) > varTexto.count(varLetraAnterior)):
        varLetraAnterior = varLetraAtual;

    

print(varLetraAnterior);