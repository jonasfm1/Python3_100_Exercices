nome = str(input('Digite seu nome completo: '))

print(f'Seu nome em MAIUSCULO ficara: {nome.upper()}')
print(f'Seu nome em minusculo ficara: {nome.lower()}')

print(f'Seu nome tem ao todo: {len(nome.replace(" ",""))}')
print(f'Seu nome tem ao todo: {len(nome.split()[0])}')