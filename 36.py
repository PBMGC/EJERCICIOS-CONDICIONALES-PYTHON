c=int(input("Cuadernos:"))
LP=0
LF=0
LL=0
if c<12: print("No recibe regalo")
elif c>=12 and c<24: 
    LL=(c//4)
    print("Recibe",LL,"lapiceros Lucas")
elif c>=24 and c<36: 
    LF=(c//4)*2
    print("Recibe",LF,"Lapiceros Faber")
else: 
    LP=(c//4)*2
    LF=(c//6)
    LL=(c//12)
    print("Recibe",LP,"Lapiceros Pilot")
    print("Recibe",LF,"Lapiceros Faber")
    print("Recibe",LL,"Lapicero Lucas")