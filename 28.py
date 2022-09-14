h=int(input("Hora:"))
horas=[1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12]

if h<=12:print(horas[h-1],"AM")
else:print(horas[h-1],"PM")
