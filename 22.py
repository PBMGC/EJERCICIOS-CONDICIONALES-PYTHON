from pydoc import describe


Pa=int(input("Unidades Producto A:"))
Pb=int(input("Unidades Producto B:"))

desc=0
ImpotA=Pa*25
ImpotB=Pb*30

if Pa>50: desc=ImpotA*0.15
else: desc=0

if Pb>60: desc=(ImpotB*0.10)+desc
else: desc=0+desc

print("Importe Bruto S/:",ImpotA+ImpotB,"\nDescuento de S/:",desc,"\nTotal a pagar S/:",(ImpotA+ImpotB)-desc)