Ht=int(input("Horas Trabajadas:"))
Cat=input("Categoria del Trabajador:")

S=0

if Cat=="A": S=Ht*21
elif Cat=="B": S=Ht*19.50
elif Cat=="C": S=Ht*17
else: S=Ht*15.50

desc=0

if S>2500: 
    desc=S*0.20
    print("!!"*2,"Descuento del 20%","!!"*2)
else: 
    desc=S*0.15 
    print("!!"*2,"Descuento del 15%","!!"*2)

print("Sueldo Bruto S/:",S,"\nDescuento S/:",desc,"\nSueldo Neto S/:",S-desc)