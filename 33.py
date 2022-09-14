T=int(input("Minutos de Tardanza:"))
O=int(input("Observaciones:"))

PT=0
PO=0
Bon=0

if T==0: PT=10
elif T<=2: PT=8
elif T<=5: PT=6
elif T<=9: PT=4
else: PT=0

if O==0: PO=10
elif O==1: PO=8
elif O==2: PO=5
elif O==3: PO=1
else: PO=0

if PT+PO<11: Bon=(PT+PO)*2.5
elif PT+PO<=13: Bon=(PT+PO)*5
elif PT+PO<=16: Bon=(PT+PO)*7.5
elif PT+PO<=19: Bon=(PT+PO)*10
else: Bon=(PT+PO)*12.5
print("Puntaje Total:",PT+PO)
print("Bonificacion S/:",Bon)
