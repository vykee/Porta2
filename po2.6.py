print("20171161")

count = 0
def contarLetras():
   count = 0
   for i in palabra:
         count += 1
   return count

palabra=(input("Introduce una palabras: "))
print(contarLetras())
