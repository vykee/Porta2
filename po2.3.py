print("20171161")
def mi_funcion(entrada):
 entrada = {}
entrada=(input("Entrar una palabra: "))
count = {}
for i in entrada:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(str(count),end='')
