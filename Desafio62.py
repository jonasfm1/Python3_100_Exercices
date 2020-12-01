print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão de PA: '))
termo = primero
cont = 1
total = 0
mais = 10
while mais != 0:
  total = total + mais
  while cont <= total:
    print(f'{termo}-> ', end='')
    termo += razão
    cont +=
  print('PAUSA')
  mais = int(input('Quantos termos você quer mostrar a mais'))
print(f'Progressão finalizada com {total} termos mostrados')