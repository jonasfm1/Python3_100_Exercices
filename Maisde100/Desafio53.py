frase = str(input('Digite uma frase: '))
palavra = frase.split()
junta = ''.join(palavra)
inversao = junto[::-1]
print(f'O inverso de {junta} é {inversao}')
if inversao == junto:
  print('Temos um palíndromo!')
else:
  print('A frase digitada não é um palindromo!')