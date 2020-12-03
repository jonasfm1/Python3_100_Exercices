import moeda
val = float(input('Digite um valor R$: '))

dobro = moeda.Dobro(val)
metade = moeda.Metade(val, True)
aumentar = moeda.Aumentar(val)
diminuir = moeda.Diminuir(val, True)

print(f'O Dobro de  {moeda.Moeda(val)} e    {dobro}')
print(f'A Metade de {moeda.Moeda(val)} e    {metade}')
print(f'Add 10% de  {moeda.Moeda(val)} fica {aumentar}')
print(f'Tira 10% de {moeda.Moeda(val)} fica {diminuir}')