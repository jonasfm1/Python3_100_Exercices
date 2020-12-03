from time import sleep

def maior(* num):
   contador = 0
   maior = 0
   print('Analisando valores...')
   for valor in num:
      print(f'{valor} ', end='', flush=True)
      sleep(0.5)
      if contador == 0:
         maior = valor
      else:
         if valor > maior:
            maior = valor
      contador += 1
   print(f'Informaram {contador} valores ao todo')
   print(f'O maior valor informado foi {maior}')


#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()