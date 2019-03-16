print("20171161")
def mi_funcion(entrada):
 entrada = 0
intentos = 0
lista=[]
while 'entrada' != 'exit':
    entrada=(input("Digite un numero: "))
    if entrada == 'exit':
     break
    lista.append(int(entrada))
m = max(lista)

print("el numero mayor de la lista es: ", m)
print("Se digito un total de: ", len(lista))
