from time import sleep
def contador(inicio, fim, pulando):
   if pulando < 0:
      pulando *= -1
   if pulando == 0:
      pulando = 1

   print(f'Contagem de {inicio} ate {fim} de {pulando} em {pulando}')
   sleep(1.0)


   if inicio < fim:
      contador  = inicio
      while contador <= fim:
         print(f'{contador} ',end='', flush=True)
         sleep(1.0)
         contador+=pulando
      print('FIM')
   else:
      contador  = inicio
      while contador >= fim:
         print(f'{contador} ',end='', flush=True)
         sleep(1.0)
         contador-=pulando
      print('FIM')


#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora Personalize a contagem a sua vontade')

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
pulando = int(input('Pulando: '))
contador(inicio, fim, pulando)