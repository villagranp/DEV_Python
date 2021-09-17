"""
Formula a realizar
(C+5)(b^2-3ac)a^2
------------------
        4a
"""
variableA = float(input('Ingrese el valor de la vaiable a: '))
variableB = float(input('Ingrese el valor de la vaiable b: '))
variableC = float(input('Ingrese el valor de la vaiable c: '))


resultado = ((variableC + 5)*(variableB**2 - (3 * variableA * variableC))) * (variableA**2) /(4 * variableA)

print(f'(',variableA,'+5)(',variableB,'^2 - 3(',variableA,')(',variableC,'))',variableA,'^2')
print('--------------------------------------------------')
print(f'                   4(',variableA,') ')
print(f'Resultado: ', resultado)
