larg = float(input('Largura da parede: '))
altu = float(input('Altura da parede: '))
area = larg * altu

print('A dimensao da parede é de {}x{} a seua area e de {}m².'.format(larg, altu, area))
tinta = area/2
print('Para pintar esta parede, precisara de {}Lt de tinta.'.format(tinta))