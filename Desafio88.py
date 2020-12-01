from random import randint
from time import sleep
lista = []
jogos = []
print('=' * 30)
print('       JOGA NA MEGA SENA      ')
print('=' * 30)
quatos_jogos = int(input('Quantos jogos voce quer sortiar: '))

compare_jogos = 1
while compare_jogos <= quatos_jogos:
  contanumeros = 0
  while True:
    numero = randint(1, 60)
    if numero not in lista:
      lista.append(numero)
      contanumeros += 1
    if contanumeros >= 6:
      break
  lista.sort()
  jogos.append(lista[:])
  lista.clear()
  compare_jogos += 1

for conj_num, lista_jogo in enumerate(jogos):
  print(f'Jogo {conj_num+1}: {lista_jogo}')
  sleep(1)
print(f'{"BOA SORTE!":>5}')