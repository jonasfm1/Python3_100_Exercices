soma = 0
cont = 0
for c in range(1 ,7):
  numero = int(input(f'Digite o {c} valor: '))
  if numero % 2 == 0:
    soma += numero
    cont += 1
print(f'Voce informou {cont} numeros PARES e a soma foi {soma}')