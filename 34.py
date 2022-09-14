Pe=float(input("Peso:"))
Es=float(input("Estatura:"))

IMC= Pe//(Es**2)

if IMC<20:print("Delgado")
elif IMC<25:print("Normal")
elif IMC<=27:print("Sobrepeso")
else: print("Obesidad")