#Exercício 040 - Aquele clássico da MÉDIA

p = float(input('Primeira nota: '))
s = float(input('Segunda nota: '))
media = (p + s) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(p,s,media))

if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO!')
elif media >= 7:
    print('O aluno está APROVADO!')
elif media < 5:
    print('O aluno está REPROVADO!')