peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC  dessa pessoa é de {imc:.1f}')

if imc < 18.5:
  print('Você está ABAIXO DO PESO NORMAL')
  
elif 18.5 <= imc < 25:
  print('PARABENS, você está na faixa do PESO NORMAL')
  
elif 25 <= imc < 30:
  print('Você está em SOBREPESO')
  
elif 30 <= imc < 40:
  print('Você esta em OBESIDADE')
  
elif imc >= 40:
  print('Você está em OBESIDADE MÓRBIDA, cuidado!')