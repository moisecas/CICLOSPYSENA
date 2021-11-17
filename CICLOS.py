#Taller 6 python
#Mosés Castro
#17 de Noviembre 2021 

from datetime import date 
hoy=date.today() #fecha actual del sistema
print("hoy es el día", hoy) 
print("")
print("taller 6 ciclos, while")
print("")
numl=int(input("digite el numero: "))
print("***ciclo controlado por contador")
i=1
while i <= numl:
    print(i)
    i += 1
print("fin del ciclo")

print()
print("***Ciclo controlado por evento")
i=1
numero1=5
numero2=int(input("digite un numero 1 a 10"))
while numero2 != numero1:
    i += 1 
    numero2=int(input("digite un numero de 1 a 10: "))
print("acertaste en el intento  No.", i)
print("fin del ciclo")
print()
print("***ciclo abortado con la sentencia break")
amistad=input("digite nombre de un amigo: ")
amistad=amistad.upper()
for character in amistad: 
    print(character)
    if character=="A":
        break
print("fin del ciclo")
print()
print("FINAL") 

