def Dobro(preco=0, formated=False):
  doble_value = preco * 2
  if formated == False:
    return doble_value
  else:
    return Moeda(doble_value)


def Metade(preco=0, formated=False):
  half_val = preco / 2
  if formated == False:
    return half_val
  else:
    return Moeda(half_val)


def Aumentar(preco=0, taxa=0, formated=False):
  up10 = (preco/100) * taxa
  moeda_mais10 = preco + up10
  if formated == False:
    return moeda_mais10
  else:
    return Moeda(moeda_mais10)


def Diminuir(preco=0, taxa=0, formated=False):
  down10 = (preco/100) * taxa
  moeda_menos10 = preco - down10
  if formated == False:
    return moeda_menos10
  else:
    return Moeda(moeda_menos10)
  


def Moeda(preco=0, moeda='R$'):
  return f'{moeda}{preco:>11.2f}'.replace('.', ',')


def Resumo(preco=0, taxaup=10, taxadown=5):
  print('='*40)
  print('RESUMO DO VALOR'.center(30))
  print('='*40)

  print(f'Preco Analizado: {Moeda(preco)}')

  print(f'Dobro do preco: \t{Dobro(preco, True)}')
  print(f'Metade do preco: \t{Metade(preco, True)}')
  print(f'Taxa de {taxaup} a menos: \t{Aumentar(preco, taxaup, True)}')
  print(f'Taxa de {taxadown} a mais: \t{Diminuir(preco, taxadown, True)}')
