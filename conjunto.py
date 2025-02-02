#Colecciones: tuplas, listas, conjuntos,  diccionarios
"""
lista = ["mazda", "renault","chevrolet"]
tupla = ("mazda", "renault","chevrolet")
conjunto = {"mazda", "renault","chevrolet"}

#conjunto no es ordernado y no puede tener elementos repetidos

conjunto.add("Audi")
print(conjunto)


conjunto.add(15)
print(conjunto)
conjunto.add(True)
print(conjunto)

#conjunto toma 0 como False y 1 como True
conjunto.add(0)
print(conjunto)
conjunto.add(False)
print(conjunto)  

conjunto = {"mazda", "renault","chevrolet"}
print(len(conjunto))

"""

conjunto = {"mazda", "renault","chevrolet"}
#conjunto.clear
""" 
conjunto2 = conjunto.copy()
print(conjunto2)
conjunto2.add("Mercedez")
print(conjunto)
print(conjunto2)
"""

"""
NO HACER
conjuntoensayis = conjunto
conjuntoensayis.add("fiat")
print(conjunto) 
"""

carros = {"mazda", "renault","chevrolet","papaya"}
colores = {"rojo", "verde", "mazda", "renault", "chevrolet"}
#print(carros.difference(colores))
#carros.discard("mazda")
#print(carros.intersection(colores))
#print(carros.issubset(colores))
#print(carros.issuperset(colores))
#print(carros)
#carros.pop()
#carros.remove("mazda")
print(carros.union(colores))
print("mazda" not in carros)
