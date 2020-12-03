def show(frase):
   tamanho = len(frase)
   print('=' * tamanho)
   print(frase)
   print('=' * tamanho)


#Programa principal
frase = str(input('Digite algo para ver uma formatacao: '))
show(frase)