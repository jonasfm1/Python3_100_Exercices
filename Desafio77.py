lista_palavras = ('chocolate', 'computador', 'aprender', 'programar', 'hacker', 'seguranca', 'serie', 'anime', 'manga', 'madara ', 'python',)

for palavra in lista_palavras:
  print(f'\nNa palavra {palavra.upper()} temos ')
  for letra in palavra:
    if letra.lower() in 'aeiou':
      print(letra, end='')