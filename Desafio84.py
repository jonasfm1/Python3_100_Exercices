list_people = []
list_all_people = []

maiorpeso = []
list_pessado = []

menorpeso = []
list_leves = []
while True:
  name = str(input('Digite o Nome: '))
  weight = float(input('Digite o peso: '))
  list_people.append(name)
  list_people.append(weight)
  list_all_people.append(list_people[:])
  list_people.clear()

  quest = str(input('Deseja continua [S/N]? ')).upper()
  if quest in 'N':
    break

print(f'\nAo todo {len(list_all_people)} pessoa(s) foram cadastradas')

for pessoa in list_all_people:
  if pessoa[1] >= 100:
    maiorpeso.append(pessoa[0])
    maiorpeso.append(pessoa[1])
    list_pessado.append(maiorpeso[:])
    maiorpeso.clear()
  else:
    menorpeso.append(pessoa[0])
    menorpeso.append(pessoa[1])
    list_leves.append(menorpeso[:])
    menorpeso.clear()

if len(list_pessado) > 0:
  print(f'As pessoas com peso acima de 100Kg sao: ')
  for pessado in list_pessado:
    print(f'{pessado[0]} ', end='')

if len(list_leves) > 0:
  print(f'\n \nAs pessoa com peso abaixo de 100Kg sao: ')
  for leve in list_leves:
    print(f'{leve[0]} ', end='')

print('\nEncerrado')