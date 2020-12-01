boletin = dict()

boletin['Aluno'] = str(input('Digite o nome do aluno: '))
boletin['media'] = float(input(f'Digite a media do {boletin["Aluno"]}: '))

if boletin['media'] < 5:
  boletin['situacao'] = 'REPROVADO'
  
elif boletin['media'] == 5:
  boletin['situacao'] = 'RECUPERACAO'

else:
  boletin['situacao'] = 'APROVADO'

print(f'O nome do Aluno(a) e {boletin["Aluno"]}')
print(f'A media do aluno e {boletin["media"]}')
print(f'Este aluno foi {boletin["situacao"]}')