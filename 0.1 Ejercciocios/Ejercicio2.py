"""
Se debe de obtener 2 valores 
posterior a eso se debe de intercambiar los valores de dichas variables

a=20  =>  a=30
b=30  =>  b=20
"""
variableA = float(input('Ingrese el valor de la vaiable a: '))
variableB = float(input('Ingrese el valor de la vaiable b: '))

print(f'variable a: ', variableA, ', variable b: ', variableB)
variableA,variableB = variableB,variableA
print(f'variable a: ', variableA, ', variable b: ', variableB)