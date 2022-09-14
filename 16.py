P_casa= int( input ( "precio de la casa:" ) )
In_Men= int( input ( "ingreso mensual:" ) )

CuotaI=0
CuotaM=0

if In_Men<1250: 
    CuotaI= P_casa*0.15
    CuotaM= (P_casa-CuotaI)/120
else: 
    CuotaI= P_casa*0.30
    CuotaM= (P_casa-CuotaI)/75

print( f"Cuota inicial de S/: {CuotaI:.1f}\nCuota Mensual de S/: {CuotaM:.1f}" )
