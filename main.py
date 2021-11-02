Lista_datos = []
while True:
    nombre = input("Introduce tu nombre: ")
    if nombre == "fin":
        break
    telefono = input("Introduce tu número de teléfono: ")

    Datos_personales = {}
    Datos_personales ["Nombre: "] = nombre
    Datos_personales ["Telefono: "] = telefono
    Lista_datos.append(Datos_personales)
for Datos_personales in(Lista_datos):
    print("Datos personales: \n", Datos_personales )






