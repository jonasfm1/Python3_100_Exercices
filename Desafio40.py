#Desafio 40
nota1 = float(input('Primeira nota'))
nota2 = float(input('Segundo nota'))
media = (nota1 + nota2) / 2

print(f'Tirando {nota1:.1f} e {nota2:.1f}, a media do aluno é {media:.1f}')
if 7 > media >= 5:
  print(f'O aluno esta em Recuperação')
elif media < 5:
  print(f'O aluno esta REPROVADO')
elif media >= 7:
  print(f'O aluno esta APROVADO')
  