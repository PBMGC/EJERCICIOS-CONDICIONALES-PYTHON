n1=int(input("Primer Numero:"))
n2=int(input("Segundo Numero:"))
n3=int(input("Tercer Numero:"))


if n1>n2:
    if n1<n3:
        print("Numero medio:",n1)
if n1<n2:
    if n1>n3:
        print("Numero medio:",n1)
if n2>n1:   
    if n2<n3:
        print("Numero medio:",n2)
if n2<n1:
    if n2>n3:
        print("Numero medio:",n2)
if n3>n1:
    if n3<n2:
        print("Numero medio:",n3)
if n3<n2:
    if n3>n2:
        print("Numero medio:",n3)
