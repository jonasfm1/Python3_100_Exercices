velocidade = float(input('Velocidade do carro: '))
if velocidade > 80: 
        print('MULTADO! VOCE EXCEDEU O LIMITE MAXIMO DE 80Km/h')
        multa = (velocidade-80) * 7
        print(f'VOCÊ DEVE PAGAR UMA MULTA DE {multa:.2f}')
print('TENHA UM BOM DIA DIRIJA COM SEGURANÇA')