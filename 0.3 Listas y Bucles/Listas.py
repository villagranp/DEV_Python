""" 
Listas
"""

array=["Futbol","PC",18.6,18,[6,7,8,9],True,False]
#todos los datos
print(array)
#primer dato
print(array[0])
#ultimo dato
print(array[-2])
#un rango de datos
print(array[0:2])

#funciones de listas
#cantidad de datos
print(len(array))
#agregar a la lista un nuevo item
array.append(66)
print(array)

#agregar a la lista un nuevo item en cierto indice
array.insert(1,88)
print(array)

#agregar a la lista un nuevo item en cierto indice
array.extend([1,90,30,True,"PC"])
print(array)
#concatenar arrays
array2 = [200,False,89]
array3 = array + array2
print(array3)

#busqueda dentro de un array (T/F)
print("PC" in array)

#busqueda dentro de un array y devolver el indice
print(array.index("PC"))

#contar veces que se repite un item Tomar en cuenta que el no. 1 se interpreta como true
print(array.count(True))

#eliminar 1 item con valor
array.remove("PC")
print(array)

#revierte el orden de los elementos
array.reverse()
print(array)

#ordena un arreglo de valores numericos
array4 = [10,50,68,1,32,-15,66]
#menor a mayor
array4.sort()
print(array4)
#mayor a menor (primero con sort se ordena)
array4.reverse()
print(array4)

