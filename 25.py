S=int(input("Sueldo: "))
H=int(input("Hijos: "))

Bon=0

if H>1: Bon=(12.5*S/100)+(H*40)
elif H==1: Bon=S*0.10
else: print("No recibe bonificacion")

print("Bonificacion de S/",Bon,"\nSueldo Neto de S/:",S+Bon)