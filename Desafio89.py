boletin = []
while True:
  nome = str(input('Nome: '))
  nota1 = float(input('Nota1: '))
  nota2 = float(input('Nota2: '))
  media = nota1 + nota2 / 2
  boletin.append([nome, [nota1,nota2], media])

  quest = str(input('Desejar Contiuar [S/N]: ')).upper()
  if quest in 'N':
    break
print('=' * 25)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('=' * 25)

for sublista, aluno in enumerate(boletin):
  print(f'{sublista:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
  print('= ' * 25)
  escolhe = int(input('Mostrar Nota de qual aluno [000]Para Sair: '))
  if escolhe == 000:
    print('Encerrenado Consulta..')
    break
  if escolhe <= len(boletin) - 1:
    print(f'Notas de {boletin[escolhe][0]} sao {boletin[escolhe][1]}')
print('.')