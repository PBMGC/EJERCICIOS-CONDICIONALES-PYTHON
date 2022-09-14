numero=int(input("Numero:"))

n1= numero // 100
n2= ( ( numero%1000 ) %100 ) //10
n3= numero%10

if n1<n2 and n1<n3: print("Orden Ascendente")
else: print("Orden Descendente")