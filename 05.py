n=int(input("ingrese el numero:"))
n1= n // 1000
n2=( n % 1000 ) //100
n3= ( ( n%1000 ) %100 ) //10
n4= n % 10

nma1=0
nma2=0
nme1=0
nme2=0

if n1==max(n1,n2,n3,n4):
    nma1=n1
    nma2=(max(n2,n3,n4))
if n2==max(n1,n2,n3,n4):
    nma1=n2
    nma2=(max(n1,n3,n4))
if n3==max(n1,n2,n3,n4):
    nma1=n3
    nma2=(max(n1,n2,n4))
if n4==max(n1,n2,n3,n4):
    nma1=n4
    nma2=(max(n1,n2,n3))

if n1==min(n1,n2,n3,n4):
    nme1=n1
    nme2=(min(n2,n3,n4))
if n2==min(n1,n2,n3,n4):
    nme1=n2
    nme2=(min(n1,n3,n4))
if n3==min(n1,n2,n3,n4):
    nme1=n3
    nme2=(min(n1,n2,n4))
if n4==min(n1,n2,n3,n4):
    nme1=n4
    nme2=(min(n1,n2,n3))

print("Numero Mayor:",str(nma1)+str(nma2))
print("Numero Menor:",str(nme1)+str(nme2))
