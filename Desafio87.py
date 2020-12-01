matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
somapar = 0
somacol = 0
maiorvalor = 0
for linha in range(0, 3):
  for coluna in range(0, 3):
    matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' * 30)
for linha in range(0, 3):
  for coluna in range(0, 3):
    print(f'[{matriz[linha][coluna]:^6}]', end='')
    if matriz[linha][coluna] % 2 == 0:
      somapar += matriz[linha][coluna]
  print()
  print(f'A soma de todos os pares e igual a {somapar}')

  for linha in range(0, 3):
    somacol += matriz[linha][2]
  print(f'A soma dos valores da terceira coluna e iagual {somacol}')

  for coluna in range(0, 3):
    if coluna == 0:
      maiorvalor = matriz[1][coluna]
    elif matriz[1][coluna] > maiorvalor:
      maiorvalor = matriz[1][coluna]
print(f'O maior valor digitado na segunda linha foi {maiorvalor}')