import time
make_list = []
for count in range(0, 5):
  make_list.append(int(input('Enter a Number: ')))

for key, value in enumerate(make_list):
  if value == max(make_list):
    print(f'The Biggest value was {max(make_list)} in position {key+1} ')
  if value == min(make_list):
    print(f'The Smaller value was {min(make_list)} in position {key+1} ')

print('Ending exercise...')
time.sleep(2)