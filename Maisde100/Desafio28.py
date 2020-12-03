from random import randint
from time import sleep
Computador = randint(0, 5) # COMPUADOR ESCOLHENDO NUEMRO DE 0 A 5

print('-=' * 20)
print('VOU PENSAR EM UM NUEMRO TENTE ADIVINHAR: ')
print('-=' * 20)

print('\n')


sleep(2)
jogador = int(input('QUAL NUMERO ESCOLHI DE 0 A 5: ')) # JOGADOR ESCOLHE UM NUEMRO

if jogador == Computador:
    print('PARABÉNS! VOCÊ ACERTOU!!')
else:
    print(f'POXA NAO FOI DESSA VEZ EU ESCOLHE {Computador} E VOCÊ {jogador}, MAS NAO DESISTA!')