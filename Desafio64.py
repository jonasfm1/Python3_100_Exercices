numero = cont = soma = 0
numero = int(input('Digite um numero [999 para parar]: '))
while numero != 999:
  soma += numero
  cont += 1
  numero = int(input('Digite um numero [999 para parar]: '))
print(f'Você digitou {cont} numeros e a soma entre eles foi {soma}')