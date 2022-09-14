Edad=int(input("edad:"))
Sexo=input("sexo:")

if Sexo=="Femenino":
    if Edad<23: print("FA")
    else: print("FB")

elif Sexo=="Masculino":
    if Edad<25: print( "MA" )
    else: print( "MB" )