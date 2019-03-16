print("20171161")

def mi_funcion(numeros):
   total = 0
   for numeros in numeros:
       total += numeros
   return total

numeros=int(input("Introduce una lista de elementos: "))
print(mi_funcion(numeros))


