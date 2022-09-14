d= int ( input ( "donacion:" ) )

centro_sa=0
comedor_ni=0
bolsa=0

if d>=10000:
    centro_sa= (d*0.30)
    comedor_ni= (d*0.50)
    bolsa= ( bolsa-( centro_sa+comedor_ni-d ) )
elif d<10000:
    centro_sa= (d*0.25)
    comedor_ni= (d*0.60)
    bolsa= ( bolsa-( centro_sa+comedor_ni-d ) ) 

print( "Presupuesto Centro de Salud S/:",centro_sa)  
print("Presupuesto Comedor de Niños S/:",comedor_ni)
print("Presupuesto para inversion S/:",bolsa )