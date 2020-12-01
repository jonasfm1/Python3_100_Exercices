from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
  print('''[1] somar
  [2] multiplicar
  [3] maior
  [4] novos numeros
  [5] sair do programa
  ''')
  opcão = int(input('>>>>> Qual é a sua opção? '))
  if opção == 1:
    soma = num1 + num2
    print(f'A Soma entre {num1} + {num2} é {soma}')
  elif opção == 2:
    produto = num1 * num2
    print(f'O resultado de {num1} x {num2} é {produto}')
  elif opção == 3:
    if num1 > num2:
      maior = num1
    else:
      maior = num2
    print(f'Entre {num1} e {num2} o maior valor é {maior}')
  elif opção == 4:
    print('Informe os numeros novamente: ')
    num1 = int(input('Primeiro valor: '))
    num2 = int(input('Segundo valor: '))
  elif opçã == 5:
    print('Finalizando...')
  else:
    print('Opção invalida. Tente novamente')
  print('=-=' * 10)
  sleep(2)
print('Fim do programa! Volte sempre!')