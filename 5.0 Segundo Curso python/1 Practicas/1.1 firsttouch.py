print("Elige tu propio camino")
startProgram = input("Escribe 'Empezar' para iniciar el programa: ")

while startProgram == 'Empezar':
    print(""" ¿Que opcion es quieres seleccionar?
          1. Quiero que me saludes 
          2. Deseo multiplicar ya que no se como se hace
          3. Quiero Salir del programa.
          """)
    option = int(input("Que opcion eliges: "))
    if option == 1:
        print("Saludos Viajero.")
    elif option == 2:
        numero1 = float(input("Ingresa el primer numero para multiplicar: "))
        numero2 = float(input("Ingresa el segundo numero para multiplicar: "))
        print(f"El resultado de la siguiente operacion {numero1} x {numero2} es: {numero1*numero2}")
    elif option == 3:
        print("Hasta pronto viajero.....")
        break
    else:
        print("opcion no reconocida. vuelve a intentarlo")


    