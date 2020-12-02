def voto(nascimento):
  from datetime import date
  now = date.today().year - nascimento
  if now < 16:
    return f'Com {now} anos: NAO VOTA.'
  elif 16 <= now < 18 or now > 65:
    return f'com {now} anos: VOTO OPCIONAL.'
  else:
    return f'Com {now} anos: VOTO OBRIGATORIO.'


#Pricipal program
nascimento = int(input('Digite o seu ano de nasciemtno: '))

resul = voto(nascimento)
print(f'{resul}')