Not_mate=int(input("Nota en Matematicas: "))
Not_fisica=int(input("Nota en Fisica: "))

pro=0

if Not_mate>17: pro=(Not_mate//3)*3
else: pro=Not_mate//1


if Not_fisica>15:pro=((Not_fisica//2)*2)+pro
else: pro=((Not_fisica//0.50)*0.50)+pro

prom=(Not_mate+Not_fisica)/2

if prom>16:
    print("!!"*3,"Gano un reloj","!!"*3)

print("Promedio:",prom,"\nPropina total S/:",pro)