print("2017116")
cantidad_estudiantes = 1
estudiantes = []
c1 = []
c2 = []
c3 =[]


while cantidad_estudiantes <= 2 :
    break

for i in range(cantidad_estudiantes):
        nombre=(input("Introduce el nombre del estudiante:"))
        estudiantes.append(nombre)
        c1=float(input("Introduce la calificacion para la quimica: "))
        c2=float(input("Introduce una calificacion para math: "))
        c3=float(input("Introduce una calificacion para fisica: "))


print(".......................................")



def cal(c2,c1,c3):
   for i in 'c2,c1,c3':
        if ('c2,c1,c3') >= 90:
            calificacion="A"
            return(calificacion)
        elif ('c2,c1,c3') >= 80:
            calificacion="B"
            return(calificacion)
        elif ('c2,c1,c3') <=70:
            calificacion="C"
            return(calificacion)
        elif ('c2,c3,c1') <=60:
            calificacion="D"
            return(calificacion)
        else:
            return(Reprobado)
print("La calificacion es: ",(cal('c1,c2,c3')))

def calcular_promedio(promedio):
    promedio=(c1,c2,c3)/3
    return promedio
print("El promedio es: ",(calcular_promedio(promedio)))

while




