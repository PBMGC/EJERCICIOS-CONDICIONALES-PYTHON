import nturl2path


codigo=int(input("Codigo:"))


n1= codigo // 1000
n2= ( ( codigo%1000 ) %1000 ) //10
n3= codigo%10

estatus=""
edad=n2
sexo=""

if n1==1:estatus="Soltero"
elif n1==2: estatus=("Casado")
elif n1==3: estatus=("Divorciado")
else: estatus=("Viudo")

if n3==1: sexo="Masculino"
else: sexo="Femenino"

print("Estatus:",estatus,"\nEdad:",edad,"\nSexo:",sexo)
