#Desafio_32
from datetime import date
ano = int(input('Que ano quer analisar ? Coloque 0 para analisar 0 ano atual: '))
if ano == 0:
  ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print(f'O ano {ano} e BISSEXTO!')
else:
  print('O ano {} NÃO é BISSEXTO')
