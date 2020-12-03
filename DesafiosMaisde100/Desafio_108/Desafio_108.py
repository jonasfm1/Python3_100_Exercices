import moeda
val = float(input('Digite um valor R$: '))

dobro = moeda.Dobro(val)
metade = moeda.Metade(val)
aumentar = moeda.Aumentar(val)
diminuir = moeda.Diminuir(val)

print(f'O Dobro de {moeda.Moeda(val)} e {moeda.Moeda(dobro)}')
print(f'A Metade de {moeda.Moeda(val)} e {moeda.Moeda(metade)}')
print(f'{moeda.Moeda(val)} MAIS 10% e igual a {moeda.Moeda(aumentar)}')
print(f'{moeda.Moeda(val)} MENOS 10% e igual a {moeda.Moeda(diminuir)}')