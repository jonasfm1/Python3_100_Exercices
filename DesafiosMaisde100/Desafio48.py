soma = 0
cont = 0
for conta in range(1, 501, 2):
  if conta % 3 ==0:
    soma += conta
    cont +=1
print(f'A soma de todos os {cont} valores solicitados é {soma}')