def fatorial(numero, show=False):
  f = 1
  for vez in range(numero, 0, -1):
    if show:
      print(vez, end='')
      if vez > 1:
        print(' x ', end='')
      else:
        print(' = ', end='')
    f = f * vez
  return f


  #Pricipal Program
  print(fatorial(5, show=True))