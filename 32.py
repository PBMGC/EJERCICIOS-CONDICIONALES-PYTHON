Ciclo=int(input("Ciclo Actual:"))
Prom=float(input("Promedio del ciclo anterior:"))

Pen=0
Desc=0

if Ciclo==1: 
    Pen=550
    print("No aplica para Descuento")
elif Ciclo==2: Pen=500
elif Ciclo==3: Pen=450
else: Pen=400

if Prom<=13.99: print("No aplica para Descuento")
elif Prom<=15.99: 
    Desc=Pen*0.10
    print("Descuento del 10%")
elif Prom<17.99: 
    Desc=Pen*0.12
    print("Descuento del 12%")
else:
    Desc=Pen*0.15
    print("Descuento del 15%")

print("Pension Actual",Pen,"\nDescuento:",Desc,"\nNueva Pension",Pen-Desc)
