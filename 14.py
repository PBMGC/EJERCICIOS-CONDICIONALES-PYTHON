compra= float( input( "monto de compra:" ) )
tar= int( input( "numero de tarjeta:" ) )

desc=0

if tar%2==0:
    desc= compra*0.15
    print( "!!"*3,"obtiene 15% de descuento","!!"*3 )
else:
    desc= compra*0.05
    print( "!!"*3,"obtiene el 5% de descuento","!!"*3 )

print( f"Descuento de S/: {desc:.1f}\nTotal a pagar S/: {compra-desc:.1f}" ) 


