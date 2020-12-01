#Desafio 39
from datetime import date
presente = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {presente}')
if idade == 18:
  print(f'Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
  saldo = 18 - idade
  print(f'Ainda faltam {saldo} anos para o alistamento')
  ano = presente + saldo
  print(f'Seu alistamento Ocorrera em {ano}')
elif idade > 18:
  saldo = idade -18
  print(f'Voce ja deveria ter se alistado ha {saldo} anos
  ano = presente - saldo
  print(f'Seu alistamento foi {ano}')