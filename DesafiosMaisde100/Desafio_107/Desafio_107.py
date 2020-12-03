import moeda
val = float(input('Digite um valor R$: '))

dobro = moeda.Dobro(val)
metade = moeda.Metade(val)
aumentar = moeda.Aumentar(val)
diminuir = moeda.Diminuir(val)

print(f'O Dobro de {val} e {dobro}')
print(f'A Metade de {val} e {metade}')
print(f'{val} MAIS 10% e igual a {aumentar}')
print(f'{val} MENOS 10% e igual a {diminuir}')