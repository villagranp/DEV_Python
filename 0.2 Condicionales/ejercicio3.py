"""
Condicionales IF
Identificar las coincidencias (Inicial y Final )
de 2 cadenas
"""
primerDato = input('Ingrese primer nombre: ')
segundoDato = input('Ingrese segundo nombre: ')

if primerDato == segundoDato: 
    print("Existe concidencia total en los valores")
elif primerDato[0] == segundoDato[0] or primerDato[-1] == segundoDato[-1]: 
    print("Existe concidencia en la primera o ultima letra")
else: 
    print("NO existe concidencia en la primera o ultima letra")
