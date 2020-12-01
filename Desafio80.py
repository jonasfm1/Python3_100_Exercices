making_list = []

for count in range(0, 5):
  new_number = int(input('Enter a number: '))

  if count == 0:
    making_list.append(new_number)

  elif new_number > making_list[-1]:
    making_list.append(new_number)

  else:
    new_number_pos = 0

    while new_number_pos < len(making_list):
      
      if new_number <= making_list[new_number_pos]:
        making_list.insert(new_number_pos, new_number)  
        break
      
      new_number_pos = new_number_pos + 1

print(f'Values in order {making_list}')