#entrada de dados
soma = 0
total_receber = 0
for i in range(2):
 horas_trab = int(input('Digite o número de horas trabalhadas: '))
 valor_hora = float(input('Digite o valor da hora trabalhada: '))
 #processamento
 total_receber = horas_trab * valor_hora
 soma = soma + total_receber
 #saída de dados
print('Total a receber:', total_receber)
print ('Soma dos totais: ' + str(soma))
if (soma > 3500):
 print ('Cumpriram a meta de horas trabalhadas !!!')
else:
 print('Não cumpriram a meta de horas !!!')
