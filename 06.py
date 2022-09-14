e1=int ( input( "primera edad:" ) )
e2=int ( input( "segunda edad:" ) )
e3=int ( input( "tercera edad:" ) )

em= 0
eme= 0

if e1>e2 and e1>e3: em=e1
else: eme=e1

if e2>e1 and e2>e3: em=e2
else: eme=e2

if e3>e1 and e3>e2: em=e3
else: eme=e3
print()
print( "La edad mayor es:",em )
print( "La edad menor es:",eme )