salario = float(input('Qual o valor do Salario ? '))
reajuste = salario + (salario* 15 /100)
print('O valor do antigo salario é de R${:.2f} com o reajuste de 15% fica R${:.2f}'.format(salario,reajuste))