pro=int ( input ( "cantidad:  " ) )

importe=pro*20
des=0

print(" **"*3, "el importe es de S/:" ,importe,"**"*3 )

if importe>=701 : des=( importe*0.16 )
elif importe<=501 or pro==700: des=( importe*0.14 )
else: des=( importe*0.12 )
print( "!!"*3,f"descuento: {des:.1f} ","!!"*3 )

print("**"*3,"Total a pagar:", importe-des ,"**"*3 ) 

if pro<=50 : print( "!!"*3 ,"Recibe 5 caramelos", "!!"*3 )
elif pro<=51 or pro==100: print( "!!"*3,"Recibe 10 caramelos","!!"*3 )
else: print( "!!"*3 ,"Recibe 15 caramelos","!!"*3 ) 
