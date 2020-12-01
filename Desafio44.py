print('{:=^40}'.format('LOJAS CHALLENGE'))
preço = float(input('Preço das compras: R$ '))
print('''ESCOLHA A FORMA DE PAGAMENTO
[1] á VISTA
[2] á VISTA CARTÃO
[3] 2x CARTÃO
[4] 3x OU MAIS NO CARTÃO
''')
opção = int(input('Qual é a opção: '))
if opção == 1:
  total = preço - (preço * 10 / 100)
elif opção ==2:
  total = preço - (preço * 5 / 100)
elif opção == 3:
  total = preço
  parcela = total / 2
  print(f'Compra parcelada em 2x de R$ {parcela:.2f} SEM JUROS')
elif opção == 4:
  total = preço + (preço * 20 / 100)
  totparc = int(input('Quantas vezes? '))
  parcela = total / totparc
  print(f'A Compra será parcelada em {totparc}x de R$ {parcela:.2f}')
else:
  total = 0
  print('OPÇÃO DE PAGAMENTO INVALIDA. Tente Novamente!')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final')