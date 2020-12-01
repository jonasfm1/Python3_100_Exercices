making_list = []

while True:
  new_value = (int(input('Enter a Number: ')))
  if new_value not in making_list:
    making_list.append(new_value)
    print('Number add! ')
  else:
    print('repeated number not enter in the list')

  question = str(input('Would you like to contiue [S/N]')).upper()
  if question in 'N':
    making_list.sort()
    break
print(f'You typed {making_list}')