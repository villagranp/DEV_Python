"""
Se debe de obtener el area y la lingitud de un circulo
A = pi * r^2
L = 2 * pi * r
"""
import math

radio = float(input('Ingrese el valor del radio del circulo: '))

area = math.pi * radio **2
longitud = 2 * math.pi * radio

print(f"El área del circulo es: {area:.1f}")
print(f"La longitud del circulo es: {longitud:.2f}")

