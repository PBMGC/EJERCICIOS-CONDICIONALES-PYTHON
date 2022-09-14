n1=int ( input( "primera nota: " ) )
n2=int ( input( "segunda nota: " ) )
n3=int ( input( "tercera nota: " ) )

puntos=0

if n3>=10: puntos=n3+2
else: puntos=n3
print( "!!"*2,"El promedio es de:",(n1+n2+puntos)//3,"!!"*2 )