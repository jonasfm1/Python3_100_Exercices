#Desafio 36
casa = float(input('Preço do imovel: R$ '))
salario = float(input('Renda liquida Comprador: R$ '))
anos = int(input('Quantas vezes deseja financiar: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 /100
print(f'Para pagar o imovel de {casa:.2f} em {anos:.2f} anos')
print(f'O financiamento ficara R${prestacao:.2f}')

if prestacao <= minimo:
  print('O Emprestimo pode ser CONCEDIDO')
else:
  print('Emprestimo NEGADO')