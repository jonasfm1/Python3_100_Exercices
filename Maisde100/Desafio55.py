maior = 0
menor = 
for p in range (1, 6):
  peso = float(input('Peso da {p}ª pessoa'))
  if p == 1:
    maior = peso
    menor = peso
  else:
    if peso > maior:
      maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso lido foi de {maior}')
print(f'O menor peso lido foi de {menor}')