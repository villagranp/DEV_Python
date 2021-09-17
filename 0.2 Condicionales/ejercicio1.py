"""
Condicionales IF
Ejericio obtener 2 numeros y obtener 
como resultado cual de ellos es par o si ambos lo son
"""
primerDato = int(input('Ingrese primer numero: '))
segundoDato = int(input('Ingrese segundo numero: '))

if primerDato%2 == 0 and segundoDato%2 == 1: 
    print("primer numero es par")
elif primerDato%2 == 1 and segundoDato%2 == 0: 
    print("Segundo numero es par")
elif primerDato%2 == 0 and segundoDato%2 == 0: 
    print("Ambos numeros son pares")
else: 
    print("ningun numero es par")
