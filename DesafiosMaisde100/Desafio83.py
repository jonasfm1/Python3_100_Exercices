expresion = str(input('Digite uma expressao: '))
list_expresion = []
for item in expresion:
  if item == '(':
    list_expresion.append('(')
  elif item == ')':
    if len(list_expresion) > 0:
      list_expresion.pop()
    else:
      list_expresion.append(')')
      break
if len(list_expresion) == 0:
  print('Expresao valida !')
else:
  print('Sua expresao esta incorreta!')