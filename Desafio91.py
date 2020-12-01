from random import randint
from operator import itemgetter
jogadores = dict()
ranking = dict()

for c in range(1,5):
  jogadores[f'jogador{c}'] = randint(1, 6)
  print(f'O jogador{c} tirou {jogadores["jogador"+str(c)]}')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-='*6,'=-'*6)

for i, v in enumerate(ranking):
  print(f'{i} lugar: {v[0]} com {v[1]}')