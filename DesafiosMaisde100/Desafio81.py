making_list = []

while True:
  new_number = int(input('Enter a Number: '))
  making_list.append(new_number)
  question = str(input('Would like to continue [S/N] ? ')).upper()
  if question in 'N':
    break

if 5 in making_list:
  print(f'The value 5 has been typed {making_list.count(5)}x and it is in the list')
else:
  print(f'The value 5 has not been typed!')

print(f'{len(making_list)} Number was typed')
print(f'descending order {sorted(making_list, reverse=True)}')
