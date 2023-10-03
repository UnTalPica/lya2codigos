#Hola Mundo 29/Agosto/2023

print("ACZINO GOAT")

#Variables

x = 7
x = "CRISTIANO"

print("Hola " + x)
x = "Messi"


#Condiciones
X = 8
nombreMessi = "Messi"
nombreCristiano = "Cristiano"
if x == 7:
    print(nombreCristiano)
elif x == 1:
    print(nombreMessi)
elif x == 4:
    print("Rafa Marquez")
else:
    print("No existe")

#Strings
nombre = "Diana"
print (nombre [0])

#Ciclos
for letra in nombre:
    print(letra)


#Imprimir Longitud
print(len(nombre))

#Comprobar si existe una cadena
texto = "Allá en la fuente había un chorrito"
print("chorrito" in texto)
if "chorrito" in texto:
    print("chorrito")





#EJERCICIO 1
"""Del siguiente texto
'Son las 7 de la noche  y ya me quiero ir'
Si encuentra el numero 7 y es menor a 8 imprimir el numero 7 
convertido a int y el texto, 'Es hora de irnos son las: '7'
"""

texto = "Son las 7 de la noche y ya me quiero ir"
if "7" in texto and int ('7') < 8:
    print (int(7))
    print("Es hora de irnos son las 7")

## Slicing String Rango
b = "Hola Mundo"
#Slice por rango
c = b[5:10]
print(c)

#Slicing desde el inicio
print(b[:5])

#Slice desde una posición hasta el final
print(b[5:])

#Slice con posiciones negativas
print(b[-5:-2])

#Boleanos
#Mayor que
print(10 > 9)

#Igual que
print (10 == 9)

#Menor que
print (10 < 9)

#Variables boleanas
enStock = True
isTiendaAbierta = True

#Uso de AND
if enStock and isTiendaAbierta:
    print("Vender productos")

tieneEfectivo = True
tieneTarjeta = True

#Uso de OR
if tieneTarjeta or tieneEfectivo:
    print ("Pago Aceptado")

regresasteConEx = False
if not regresasteConEx:
    print("Mentiroso!!!")

paseLenguajes = True
if not paseLenguajes:
    print("Reprobaste")
else:
    print("Si pasaste")

isUploaded = False
if not isUploaded:
    print("Reintentar")

#OPERADORES ARITMÉTICOS
x = 5
y = 6
#SUMA
print(x + y)
#RESTA
print(x - y)
#MULTIPLICACION
print(x * y)
#DIVISION
print(x / y)
#Modulo
print(x % y)
#Exponentes
print(2 ** 2)
print(x ** 2)
print(x ** y)
#Floor Division
print(4 // 2)
print(x // y)

#Operadores de Asignación
x = 30
x += 32
x -= 2
x *= 2
x /= 2
print(x)

#Operadores Lógicos Comparación
a = 3
b = 2
#Igual
print(a == b)
#Diferente
print(a != b)
#Mayor
print(a > b)
#Menor
print (a < b)
#Mayor igual
print(a >= b)
#Menor igual
print(a <= b)

# Operadores Lógicos
promedio = 100
asistencias = True
aprobado =(promedio > 70) and asistencias
#and, or, not
print(aprobado)

# Operadores de Identidad
j = "HOLA"
k = "HOLA "
print(k.replace(" ", ""))
print(j is k.replace(" ", ""))
print(j is not k)

# Operadores de pertenencia
print("A" in "HOLA")
print("A" not in "HOLA")

#lista
frutas = ["Manza", "Plaatano", "Sandia"]
print(frutas)

##Listas, tuple , set , dictonary
#Tuple: es una coleccion la cual esta ordenada y no es modificable. permite duplicados
#set: Es una coleccion la cual no esta ordenada y no es modificable no inexada. No permite duplicado
#Dictonary: Es una coleccion la cual esta ordenada es modificable. No permite duplicados

#lista
lista1 = tupla1 = ["🐯", "👽 ", " 🦁"]
lista1.insert(3,"🙊")
lista1 [2] = "🦓"
print(lista1)

#tupla
tupla1 = ("🐯", "👽 ", " 🦁")
print(tupla1)

#set
set1 = {"🐯", "👽 ", " 🦁"}
set1.add("🦅")
set1.add("🐺")
set1.add("🦝")
print(set1)

#diccionario
diccionario1 = {
    "tigre": "🐯",
    "los estraterrestres": "👽",
    "leon": "🦁"
}
diccionario1["mapache"] = "🦝"
diccionario1["lobo"] = "🐺"
print(diccionario1["lobo"])
print(diccionario1)

"""CREAR UNA LISTA: 1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9
1. CONVERTIR LA LISTA EN UN SET PARA ELIMINAR DUPLICADOS
2. CALCULAR LA SUMA DE LOS NÚMEROS USANDO UNA LISTA
3. CALCULAR LA SUMA DE LOS NÚMEROS USANDO UN SET
4. CREAR UN DICCIONARIO PARA ALMACENAR LAS ESTADÍSTICAS
    NÚMEROS ÚNICOS, SUMA TOTAL LISTA, SUMA TOTAL SET
    MAXIMO VALOR, MINIMO VALOR 
    IMPRIMIR LAS ESTADÍSTICAS"""
#Lista numeros
numeros = [1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9]
#Set de la lista
numerosSet = set(numeros)
#Suma de los numeros usando una lista
sumaLista = sum(numeros)
#Suma de los numeros usando un set
sumaSet = sum(numerosSet)
#Numero maximo lista
maxNumeros = max(numeros)
#Numero minimo lista
minNumeros = min(numeros)
diccEstadistica = {
    "numerosSet": len(numerosSet),
    "SumaLista": sumaLista,
    "SumaSet": sumaSet,
    "Maximo Valor": maxNumeros,
    "Minimo Valor": minNumeros
}
print(diccEstadistica)



# CONDICIONES
a = 200
b = 33

if b > a:
    print("b es mayor que a")
elif a == b:
    print("a y b son iguales")
else:
    print("a es mayor que b")



# CICLO WHILE

quiereVolver = True
vecesRegresaron = 0
while vecesRegresaron < 3:
    vecesRegresaron += 1
    print("Han vuelto " + str(vecesRegresaron) + " veces")


print("Break")
# BREAK
i = 8
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("i es == a 3")

print("Continue")
# CONTINUE
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# CICLO FOR - FOR EACH
frutas = ["🍎","🍌","🥭"]

# FOR - POR CADA
buscar = True
if buscar:
    for fruta in frutas:
        if fruta == "🍌":
            print("Se encontró: "+ fruta)
        else:
            print("NO COINCIDE")

else:
    print("No se está buscando")