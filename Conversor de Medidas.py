medida = float(input('Digite uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida / 10
hm = medida / 100
km = medida / 1000

print('A medida de {}m corresponde a {:.0f}cm\n  {}mm\n {}dm\n {}hm\n {}km'.format(medida, cm, mm, dm, hm, km))
