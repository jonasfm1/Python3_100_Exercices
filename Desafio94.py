galera = list()
pessoa = dict()
soma = 0
media = 0

while True:
  pessoa.clear()
  pessoa['nome'] =  str(input('Nome: '))
  while True:
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    if pessoa['sexo'] in 'MF':
      break
    print('ERRO! Por favor digite M ou F')
  pessoa['idade'] = int(input('Idade: '))
  soma += pessoa['idade']
  galera.append(pessoa.copy())
  while True:
    quest = str(input('Quer continuar [S/N] ')).upper()[0]
    if quest in 'SN':
      break
    print('ERRO! Digite Apenas S para SIM ou N para NAO')
  if quest == 'N':
    break
print('\n')

print(f'Ao todos temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A media de idade e de {media:5.2f} anos')
print(f'As Mulheres cadastradas foram: ')
for pessoa in galera:
  if pessoa['sexo'] in 'Ff':
    print(f'{pessoa["nome"]} ', end='')

print('A lista de pessoa que estao acima da media: ')
for pessoa in galera:
  if pessoa['idade'] >= media:
    for k, v in pessoa.items():
      print(f'{k} = {v}; ', end='')
    print()
print('ENCERRANDO')