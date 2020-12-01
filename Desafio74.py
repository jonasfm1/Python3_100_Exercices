from random import randint
numerospc = ((randint(1, 10)), (randint(1, 10)), (randint(1, 10)),
            (randint(1, 10)),(randint(1, 10)))
print('Os valores sorteados foram: ', end='')
for n in numerospc:
  print(f'{n}', end='')
print(f'\nO maior valor sorteado foi {max(numerospc)}')
print(f'O menor valor sorteado  foi {min(numerospc)}')
