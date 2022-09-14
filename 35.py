cod=int(input("Codigo:"))

if cod%2==0 and cod%3==0 and cod%5==0: print("Empleado Administrativo")
elif cod%3==0 and cod%5==0: print("Empleado Directivo")
elif cod%2==0: print("Empleado Vendedor")
else: print("Empleado de Seguridad")