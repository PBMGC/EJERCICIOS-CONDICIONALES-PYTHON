DP=int(input("Dia del pago:"))
P=float(input("Cuota del mes:"))

desc=0
recar=0

if DP<=10: desc=(P*0.02)
else: recar=(P*0.03)

if desc==5 or desc==2*P/100:
    if desc<=5: desc=5 , print("Descuento del 2%","\nDescuento S/:",desc,"\nCuota neta del mes:",P-desc)
    else: desc=(P*0.02) , print("Descuento del 2%","\nDescuento S/:",desc,"\nCuota neta del mes:",P-desc)

if recar==10 or recar==3*P/100:
    if recar<=10: recar=10 , print("Recargo del 3%","\nRecargo S/:",recar,"\nCuota neta del mes S/:",P+recar)
    else: recar=(P*0.03) , print("Recargo del 3%","\nRecargo S/:",recar,"\nCuota neta del mes S/:",P+recar)