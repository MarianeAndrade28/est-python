# Exercício 011 - Pintando a parede
larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg,alt,area))
print('Sabendo que 1 litro pinta 2m², você precisará de: {:.1f}l de tinta para pintar sua parede'.format(tinta))