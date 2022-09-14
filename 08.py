ex1= str( input ( "Status del primer examen:" ) )
ex2= str( input ( "Status del segundo examen:" ) )
ex3= str( input ( "Status del tercer examen:" ) )

pro=20

if ex1=="Aprobado" or ex1=="A" or ex1=="aprobado": pro=pro+5

if ex2=="Aprobado" or ex2=="A" or ex2=="aprobado": pro=pro+5

if ex3=="Aprobado" or ex3=="A" or ex3=="aprobado": pro=pro+5

print("Su propina es de S/:",pro)

