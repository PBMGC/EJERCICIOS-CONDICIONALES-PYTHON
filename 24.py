Venta=int(input("Monto vendido: "))

Exceden=0
comision=Venta*0.10

if Venta>5000:
    Exceden=((Venta-5000)/500)*25

print("Sueldo S/:",comision+Exceden)
