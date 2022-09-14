HT=int(input("Horas Trabajadas:"))
PH=float(input("Pago por Hora:"))

HE=0
sueldo=(HT*PH)+HE
desc=0

if HT>48: 
    HE=(sueldo*0.20)+sueldo
    print("Recargo del 20%")

if sueldo>1500:
    desc=(sueldo*0.10)
    print("Descuento del 10%")

print("\nSueldo Bruto S/:",sueldo,"\nDescuento S/:",desc,"\nSueldo Neto S/:",(sueldo+HE)-desc)