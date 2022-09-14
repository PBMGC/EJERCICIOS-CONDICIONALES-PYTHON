n1=int ( input ( "primera nota:" ) )
n2=int ( input ( "segunda nota:" ) )
n3=int ( input ( "tercera nota:" ) )
n4=int ( input ( "cuarta nota:" ) )
n5=int ( input ( "quinta nota:" ) )

nma=0
nme=0

if n1>n2 and n1>n3 and n1>n4 and n1>n5: nma=n1
elif n2>n1 and n2>n3 and n2>n4 and n2>n5: nma=n2
elif n3>n1 and n3>n2 and n3>n4 and n3>n5: nma=n3
elif n4>n1 and n4>n2 and n4>n3 and n4>n5: nma=n4
else: nma=n5

if n1<n2 and n1<n3 and n1<n4 and n1<n5: nme=n1
elif n2<n1 and n2<n3 and n2<n4 and n2<n5: nme=n2
elif n3<n1 and n3<n2 and n3<n4 and n3<n5: nme=n3
elif n4<n1 and n4<n2 and n4<n3 and n4<n5: nme=n4
else: nme=n5

prom=(n1+n2+n3+n4+n5-nma-nme)/3

print( f"Promedio:{prom:.1f}\nNota Mayor: {nma}\nNota Menor: {nme}" )


