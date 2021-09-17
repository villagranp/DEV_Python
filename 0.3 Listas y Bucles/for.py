#bucles (while y For)
data = [ 1,2,13,54,5,26,7,8,89, "PC" ]
for i in data:
    print(f"el valor de i : {i}")


#Ejercicio1 - FOR
#sumar todos los numeros entre 1 y 100
sumatoria = 0

for i in range(1, 101, 1):
    sumatoria += i
    
print(f"La sumatoria de los numeros es: {sumatoria}")
