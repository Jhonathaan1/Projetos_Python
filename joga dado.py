from random import randint as r

def telesena():
    num = r(1,999)#numeros aleatorio entre 1 e 6
    return num

for x in range(6):
        n = telesena()
        print('numeros telesena:', n)
