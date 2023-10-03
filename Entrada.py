# ENTRADA DE DATOS
print("Ingresa nombre:")
nombre = input()
palabras = nombre.split(" ")
nombreCapitalizado = ""

for palabra in palabras:
    nombreCapitalizado += palabra.capitalize() + " "
print(nombreCapitalizado)
