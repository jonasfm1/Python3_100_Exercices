#Desafio_33
a = int(input('Primeiro valor'))
b = int(input('Primeiro valor'))
c = int(input('Primeiro valor'))

#Verificar quem é menor
menor = a
if b < a and b < c:
  menor = b
if c < a and c < b:
  menor = c
print(f'O menor valor digitado foi {menor}')

#Verificar quem é o maior
maior = a
if b > a and b > c:
  maior = b
if c > a and c > b:
  maior = c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')