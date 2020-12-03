from datetime import datetime
data_atual = datetime.now()
cidadao = dict()

cidadao['nome'] = str(input('Digite o Nome: '))
cidadao['idade'] = data_atual.year - int(input('Ano de nascimento: '))
cidadao['ctps'] = int(input('carteira de trabalho: '))

if cidadao['idade'] > 0:
  cidadao['trabalha_faz'] = data_atual.year - int(input('Ano de contracao: '))
  tempo_de_ctps = 35 - cidadao['trabalha_faz']
  cidadao['Ano_de_aposentadoria'] = cidadao['idade'] + tempo_de_ctps

print(f'='*5,'{Dados Complementares}','='*5)
for key, value in cidadao.items():
  print(f'{key} e {value}')
