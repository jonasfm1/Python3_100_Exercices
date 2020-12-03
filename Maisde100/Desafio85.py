valores = [[],[]]
number = 0
for c in range(0, 7):
  number = int(input(f'Digite o {c}o valor: '))
  if number % 2 == 0:
    valores[0].append(number)
    
  else:
    valores[1].append(number)

valores[0].sort()
valores[1].sort()

print(f'Valores impares na lista em ordem Cresente {valores[0]}')

print(f'Valores par na lista em ordem Decrescente {valores[1]}')