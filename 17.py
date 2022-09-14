docenas=int(input("Docenas Compradas: "))
pre=float(input("Precio por Docena: "))

monto=docenas*pre
desc=0
lapicero=0


if docenas>=6:desc=monto*0.15
else: desc=monto*0.10

if docenas>=30: 
    lapicero=(docenas//3)*2
    print("Obsequio de",lapicero,"lapiceros")
else:
    print("No recibe obsequio")

print(f"El monto sin descuento S/: {monto:.1f}")
print(f"Descuento de S/: {desc:.1f}") 
print(f"Total a pagar S/: {monto-desc:.1f}")