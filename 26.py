compra=int(input("Monto total de compra: "))

prestamo=0

if compra>5000: 
    prestamo=(compra*0.30)
    print("Solicitar prestamo del 30%")
else: 
    prestamo=(compra*0.20)
    print("Solicitar prestamo del 20%")

interes=prestamo*0.10

print("Prestamo de $:",prestamo,"\nInteres de $:",interes,"\nTotal a cubrir $:",compra-prestamo)