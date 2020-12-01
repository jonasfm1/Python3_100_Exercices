numero = int(input('Digite um numero para calcular o Fatorial'))
c = numero
fa = 1
print(f'Calculando {numero}! =', end='')
while c > 0:
  print(f'{c}', end='')
  print('x' if c > 1 else ' = ', end='')
  fa *= c
  c -= 1
print(f'{fa}')