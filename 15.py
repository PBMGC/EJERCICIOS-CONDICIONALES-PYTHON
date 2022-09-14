venta= int( input ( "monto total vendido:" ) )

comision= 0

if venta<5000: comision= venta*0.05
elif venta==5000 or venta<10000: comision= venta*0.08
elif venta==10000 or venta<20000: comision= venta*0.10
else: comision= venta*0.15

sueldo= 250+comision
desc=0

if sueldo>3500: desc= sueldo*0.15
else: desc= sueldo*0.08

print( f"Su comision es de S/: {comision:.1f}")
print(f"Sueldo bruto S/: {sueldo:.1f}")
print(f"El descuento es de S/: {desc:.1f}")
print(f"El sueldo neto es de S/: {sueldo-desc:.1f}")
