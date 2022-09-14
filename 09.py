cod= int ( input ( "codigo: " ) )
unidades= int ( input ( "unidades: " ) )

importe=0
desc=0

if cod==101: importe=unidades*17
elif cod==102: importe=unidades*25
elif cod==103: importe=unidades*16
elif cod==104: importe=unidades*27

if unidades<=10: desc=importe*0.05
elif unidades>=11 and unidades<=20 : desc=importe*0.08
elif unidades<=21 or unidades==30: desc=importe*0.10
elif unidades>30: desc=importe*0.13

print( f"El importe es de S/: {importe:.1f}" )
print(f"Descuento de S/: {desc:.1f}" )
print(f"El total a pagar es de S/: {importe-desc:.1f}")