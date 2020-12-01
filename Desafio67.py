while True:
  ntabu = int(input('Quer ver a tabuada de qual valor '))
  print('-' * 30)
  if n < 0:
    break
  for c in range(1, 11):
    print(f'{ntabu} X {c} = {n*c}')
  print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. volte sempre!')