#Desafio 37
numero = int(input('Digite um numero Inteiro'))
print('''Escolha o tipo de CONVERSÂO
[1]converter para Binario
[2]converter para OCTAL
[3]converter para HEXADECIMAL ''')
escolha = int(input(Sua opcao: ))
if opcao ==1:
  print(f'{numero} convertido para BINARIO é igual a {bin(numero)[2:]}')
elif:
  print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif:
  print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
  print('Opção invalida tente novamente')