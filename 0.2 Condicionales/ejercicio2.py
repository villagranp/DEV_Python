"""
Condicionales IF
Ejericio obtener 3 numeros y
determinar cual de los 3 es el mayor
"""
primerDato = int(input('Ingrese primer numero: '))
segundoDato = int(input('Ingrese segundo numero: '))
tercerDato = int(input('Ingrese tercer numero: '))

if primerDato < segundoDato: 
    if segundoDato < tercerDato:
        print("el tercer numero es el mayor")
    else:
        print("el segundo numero es el mayor")
elif primerDato < tercerDato: 
    if tercerDato < segundoDato:
        print("el segundo numero es el mayor")
    else:
        print("el tercer numero es el mayor")
else: 
    print("el primer numero es el mayor")
