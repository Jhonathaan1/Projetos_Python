# Aula 10 - Jogo que simula uma moeda cara ou coroa
from random import *


def joga_moeda():  # Função
    pass  # ignorado pelo interpretador

    valor = random()  # numero entre 0 e 9
    #print(valor)
    
    if valor > 0.5:
        return 'Cara'
    else:
        return 'Coroa'
        

moeda = joga_moeda()
print(moeda)
