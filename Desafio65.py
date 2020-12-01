resposta = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
  num = int(input('Digite um numero: '))
  soma += num
  quant =+ 1
  if quant == 1:
    maior = menor = num
  else:
    if num > maior:
      maior = num
    if num < menor:
      menor = num
  resposta = str(input('Quer Continua [S/N]: ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} numeros e a média foi {media}')
print(f'O Maior valor foi {maior} e o menor foi {menor}')
