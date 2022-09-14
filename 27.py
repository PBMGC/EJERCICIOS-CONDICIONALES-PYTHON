MV=int(input("Monto total vendido:"))

suelB=600+(MV*0.15)
desc=0

if suelB>1800: 
    desc=(suelB*0.10)
    print("Descuento del 10%")
else: 
    desc=(suelB*0.05)
    print("Descuento del 5%")

if MV>1000:print("Obsequio de 3 polos")
else: print("Obsequio 1 polo")

print("Sueldo Bruto S/:",suelB,"\nDescuento S/:",desc,"\nSueldo Neto S/",suelB-desc)
