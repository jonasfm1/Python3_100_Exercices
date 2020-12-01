jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: '))
totalpartidas = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou: '))

for vez in range(1, totalpartidas+1):
  partidas.append(int(input(f'  Quantos gols na partida {vez}? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

for key, value in jogador.items():
  print(f'O campo {key} tem o valor {value}')
print('\n')

print(f'O Jogador {jogador["nome"]} Jogou {len(jogador["gols"])} partidas')

for vez, value in enumerate(jogador['gols']):
  print(f' => Na partida {vez+1}, fez{value} gols')

print(f'Foi um total de {jogador["total"]} gols')