n1=int(input("Primer Numero: "))
n2=int(input("Segundo Numero: "))
n3=int(input("Tercer Numero: "))

if n1<n2 and n1<n3: print("Orden Ascendente")
elif n1>n2 and n1>n3: print("Orden Descendente")
else: print("Numeros en desorden")