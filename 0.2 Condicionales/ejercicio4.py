"""
Condicionales IF
Cajero con opciones Saldo Inicial 2000
1. Ingreso de dinero
2. Rerirar dinero
3. Mostrar saldo
4. salir
"""
saldo = 2000
print("Cajero Automatico.")
print("Opciones:")
print("1. Ingreso de dinero")
print("2. Rerirar dinero")
print("3. Mostrar saldo")
print("4. salir")
option = int(input('Digite opcion a realizar: '))

if option == 1:
    deposit = float(input('monto a ingresar: '))
    saldo += deposit
    print(f"nuevo saldo: {saldo:.2f}")
elif option == 2:
    retire = float(input('monto a retirar: '))
    if retire > saldo :
        print("Saldo insuficiente")
    else :
        saldo -= retire
        print(f"nuevo saldo: {saldo:.2f}")
elif option == 3:
    print(f"saldo actual: {saldo:.2f}")
else:
    print('Adios')