#conjuntos

a = {1,2,3,4}
b = {2,3,5,6}
c = {3,4,6,7}

#comparacion
print(a == b)

#union AUB
print(a|b)
#union AUC
print(a|c)
#union BUC
print(b|c)


#Interseccion ANB
print(a&b)
#Interseccion ANC
print(a&c)
#Interseccion BNC
print(b&c)

#diferencia A-B
print(a-b)
#diferencia A-C
print(a-c)
#diferencia B-C
print(b-c)

#diferencia simetrica A-B U B-A
print(a^b)
#diferencia simetrica A-C U C-A
print(a^c)
#diferencia simetrica C-B U B-C
print(b^c)






