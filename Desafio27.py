fullname = str(input('Digite seu nome completo: ')).strip().upper().split()

print(f'Seu Primeiro nome é: {fullname[0]}')

print(f'Seu Ultimo nome é: {fullname[len(fullname)-1]}')