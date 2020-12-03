str_numero = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
          'onze','doze','treze','quartoze','quinze','dezeseis','dezesete','dezoito','dezenove', 'vinte')

while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('erro tente novamente')
print(f'Voce digitou o numero {str_numero[numero]}')
