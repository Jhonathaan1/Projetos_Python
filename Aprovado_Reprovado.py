#Ciencias da Computação
#Aluno: Jhonathan da S. Amorim
#matricula: 202208845282




nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
if media == 10:
    print('Aprovado com Distinção.')
elif media >= 7 and media < 10:
    print('Aprovado.')
else:
    print('Reprovado.')
