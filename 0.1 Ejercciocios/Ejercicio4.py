"""
Se debe de obtener el precio final
si al valor de la venta se le realiza un descuento del 36% al total de la compra
"""
import math
DESCUENTO = 36
MONEDA = 'GTQ.'
precio = float(input('Ingrese el valor del precio total de la compra: '))

preciofinal = precio * (1 - (DESCUENTO/100))
print(f"El total final a pagar es de: {MONEDA}{preciofinal:.2f}")