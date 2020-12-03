from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0]
[1]
[2]
''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Computador jogou {itens[jogador]}')
print('-=' * 11)

if computador == 0: #computador jogou PEDRA
  if jogador == 0:
    print('EMPATE')
  if jogador == 1:
    print('JOGADOR VENCE')
  if jogador == 2:
    print('COMPUTADOR VENCE')
  else:
    print('JOGADA INVALIDA!')

elif computador == 1: #computador jogou PAPEL
  if jogador == 0:
    print('COMPUTADOR VENCE')
  if jogador == 1:
    print('EMPATE')
  if jogador == 2:
    print('JOGADOR VENCE')
  else:
    print('JOGADA INVALIDA!')
    
elif computador == 2: #compuatador jogou TESOURA
  if jogador == 0:
    print('JOGADOR VENCE')
  if jogador == 1:
    print('COMPUTADOR VENCE')
  if jogador == 2:
    print('EMPATE')
  else:
    print('JOGADA INVALIDA!')