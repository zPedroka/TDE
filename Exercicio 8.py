from cmath import pi


altura=float(input("qual é a altura"))
raio=float(input("qual é o raio"))
area=(2*altura*raio*pi)
area2=pi*(raio**2)
areaT=2*area2+area
tinta=areaT/15
custo=tinta*50
print(custo, tinta)