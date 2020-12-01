make_list = []
make_list_impar = []
make_list_par = []
while True:
  new_number = int(input('Enter a Number: '))
  question = str(input('Would you like to continue [S/N]: ')).upper()
  make_list.append(new_number)

  if new_number % 2 == 0:
    make_list_par.append(new_number)
  else:
    make_list_impar.append(new_number)

  if question in 'N':
    break
print(f'General list {make_list}')
print(f'list of Par number {make_list_par}')
print(f'list os Impar number {make_list_impar}')
