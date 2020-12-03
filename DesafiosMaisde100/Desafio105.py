def notas(*numero, sit=False):
  quest = dict()
  quest['total'] = len(numero)
  quest['maior'] = max(numero)
  quest['menor'] = min(numero)
  quest['media'] = sum(numero) / len(numero)
  
  if sit:
    if quest['media'] >= 7:
      quest['situacao'] = 'BOA'
    elif quest['media'] >= 5:
      quest['situacao'] = 'RAZOAVEL'
    else:
      quest['situacao'] = 'RUIM'
  return quest


#Pricipal Program
resposta = notas(5.5, 3.3, 1.1, sit=True)
print(resposta)