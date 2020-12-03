'''co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = (co**2 + ca**2)**(1/2) # **(1/2) calculo de raiz quadrada cassim como ** 0.5
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

#Com uso de Bibliote
from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))