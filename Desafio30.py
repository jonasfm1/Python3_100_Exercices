num = (int(input('Digite um nuemro para saber se ele e IMPAR ou PAR: ')))
calc = num % 2

if calc == 0:
    print(f"0 numero {num} e PAR")
else:
    print(f'O numero {num} e IMPAR')