#Desafio_31
distancia = float(input('Qual é a distancia da sua viagem: '))
print(f'você está prestes e começar uma viagem de de {distancia}')
preço = distancia * 0.50

if distancia <= 200:
  preço = distancia * 0.50
else:
  preço = distancia * 0.45
  
print(f'O preço da sua passagem sera de R$ {preço:.2f}')