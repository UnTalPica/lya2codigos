# FUNCIONES

x = 1
print(x)

# CREAR FUNCIONES CON PARAMETROS FINITOS Y KEYWORDS
def saludar(nombre, edad):       #DECLARACION DE NUEVA FUNCIÓN
    print("Hola " + nombre + " Edad: " + str(edad))

if x == 1:
    saludar(edad = 20, nombre = "Leydi")
if x == 2:
    saludar("Luiz", 20)

while x < 6:
    saludar("Victor", 25)
    x+= 1

saludar("Ficachi", 22)
saludar("Rolex", 21)

# FUNCIONES CON N PARAMETROS
def asistencia(*alumnos):
    for alumno in alumnos:
        print("ASISTIÓ:" + alumno)

asistencia("Laura", "Angel", "Octavio")
asistencia("CJ","angel", "kevin", "cesar", "Michelle")

