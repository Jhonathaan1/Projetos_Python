dias = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quantos KM rodados? '))
resultado = (dias * 60) + (km*0.15)
print('o Valor total ficou em {:.2f}'.format(resultado))