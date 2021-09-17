#bucles (while y For)
import math

numero = 0
while numero <= 20:
    print(numero)
    numero +=1
    
numero2 = int(input("Ingrese un numero: "))
#obtener raiz cuadrada de un numero
while numero2 < 0:
    print("Favor ingrese un numero positivo.")
    numero2 = int(input("Ingrese un numero: "))
    
print(f"la raiz cuadrada del numero es: { math.sqrt(numero2) }")