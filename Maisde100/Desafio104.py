def leiaInt(menssage):
  ok = False
  valor = 0
  while True:
    n = str(input(menssage))
    if n.isnumeric():
      valor = int(n)
      ok = True
    else:
      print('\033[0;31,mERROR! Digite um numero inteiro.\33[m')
    if ok:
      break
  return valor


#Priciapl program
n = leiaInt('Digite um numero:')
print(f'Voce acabou de digitar o numero {n}')