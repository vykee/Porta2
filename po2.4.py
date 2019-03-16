print("20171161")

def mi_funcion(entrada):
    count = 0
    for entrada in entrada:
        if (len(entrada) >= 2) and (entrada[0] == entrada[len(entrada)-1]):
            count = count + 1
    return count

entrada=(input("Introduce una lista: "))
entrada=entrada.split(",")
print(mi_funcion(entrada))

