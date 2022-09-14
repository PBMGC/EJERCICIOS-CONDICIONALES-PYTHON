from tkinter import N


PCM1=int(input("Nota Primera Practica Calificada Matematica:"))
PCM2=int(input("Nota Segunda Practica Calificada Matematica:"))
PCM3=int(input("Nota Tercera Practica Calificada Matematica:"))
EPM=int(input("Nota Examen Matematica Parcial:"))
EFM=int(input("Nota Examen MAtematica Final:"))
print()
PCF1=int(input("Nota Primera Practica Calificada Fisica:"))
PCF2=int(input("Nota Segunda Practica Calificada Fisica:"))
PCF3=int(input("Nota Tercera Practica Calificada Fisica:"))
EPF=int(input("Nota Examen  Fisica Parcial:"))
EFF=int(input("Nota Examen  Fisica Final:"))
print()
PCQ1=int(input("Nota Primera Practica Calificada Quimica:"))
PCQ2=int(input("Nota Segunda Practica Calificada Quimica:"))
PCQ3=int(input("Nota Tercera Practica Calificada Quimica:"))
EPQ=int(input("Nota Examen  Quimica Parcial:"))
EFQ=int(input("Nota Examen  Fisica Final:"))

NM=(PCM1*0.10)+(PCM2*0.20)+(PCM3*0.10)+(EPM*0.30)+(EFM*0.30)
NF=(PCF1*0.20)+(PCF2*0.20)+(PCF3*0.20)+(EPF*0.20)+(EFF*0.20)
NQ=(PCQ1*0.10)+(PCQ2*0.30)+(PCQ3*0.10)+(EPQ*0.25)+(EFQ*0.25)
Prom=(NM+NF+NQ)//3
if Prom>=13:
    print("Aprobado")
    print(f"Promedio Matematica:{NM:.1f}")
    print(f"Promedio Fisica:{NF:.1f}")
    print(f"Promedio Quimica:{NQ:.1f}")
    print(f"Promedio General:{Prom:.1f}")
else:
    print("Desaprobado")
    print(f"Promedio Matematica:{NM:.1f}")
    print(f"Promedio Fisica:{NF:.1f}")
    print(f"Promedio Quimica{NQ:.1f}")
    print(f"Promedio General:{Prom:.1f}")