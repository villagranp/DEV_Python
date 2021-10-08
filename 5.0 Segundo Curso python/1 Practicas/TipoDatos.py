"""
Ejercicios de Tipos de Datos Simples
Ejercicio 1
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
"""
print("Hola Mundo")

"""
Ejercicio 2
Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
"""
myVar = "Hola Mundo"
print(myVar)

"""
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre 
por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
"""
nombre = input("Ingresa tu nombre: ")
print("¡Hola, {}!".format(nombre))

"""
Ejercicio 4
Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
((3+2)/(2*5))^2
"""
resultado = ((3+2)/(2*5))**2
print("el resultado de la operación ((3+2)/(2*5))^2 es: {}".format(resultado))
"""
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.
"""
horasTrajabadas = int(input("Ingrese cantidad de horas trabajadas: "))
costoHora       = float(input("Ingrese el costo de cada hora trabajada: "))
totalPago = horasTrajabadas * costoHora
print("por {} horas trabajadas su paga sera de: {}".format(horasTrajabadas, totalPago))

"""
Ejercicio 6
Escribir un programa que lea un entero positivo, n , introducido por el usuario y después muestre en pantalla la suma de 
todos los enteros desde 1 hasta . La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma:
"""

entero = int(input("Ingrese un numero entero positivo: "))
sumaEnteros = (entero * ( entero + 1))/2
print("la suma de enteros del 1 hasta el {} es: {}".format(entero, sumaEnteros) )

"""
Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla 
la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu estatura en metros: "))
imc = ((peso)/(altura **2))
print(f"Tu indice de masa corporal es <imc>{imc:.2f}<imc>" )

"""
Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
"""
"""
Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""
"""
Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""
"""
Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""
"""
Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
"""