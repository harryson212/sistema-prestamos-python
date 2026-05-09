
equipos = {
    "Laptop HP": {
        "disponible": True,
        "prestamos": []
    },
    "Proyector Epson": {
        "disponible": True,
        "prestamos": []
    },
    "Tablet Samsung": {
        "disponible": True,
        "prestamos": []
    }
}



def mostrar_equipos():
    print("\n===== LISTA DE EQUIPOS =====")

    for nombre, datos in equipos.items():

        if datos["disponible"]:
            estado = "Disponible"
        else:
            estado = "Prestado"

        print(f"- {nombre}: {estado}")



def registrar_prestamo():

    mostrar_equipos()

    equipo = input("\nIngrese el nombre exacto del equipo: ")

 
    if equipo not in equipos:
        print("El equipo no existe en el sistema.")
        return

    # Validar disponibilidad
    if not equipos[equipo]["disponible"]:
        print("El equipo ya está prestado.")
        return

    usuario = input("Ingrese el nombre del usuario: ")
    fecha = input("Ingrese la fecha del préstamo: ")

   
    prestamo = (usuario, fecha)

    
    equipos[equipo]["prestamos"].append(prestamo)


    equipos[equipo]["disponible"] = False

    print("Préstamo registrado correctamente.")



def devolver_equipo():

    equipo = input("\nIngrese el nombre exacto del equipo a devolver: ")

    # Verificar si existe
    if equipo not in equipos:
        print("El equipo no existe.")
        return

    # Verificar si está prestado
    if equipos[equipo]["disponible"]:
        print("El equipo ya está disponible.")
        return

    # Cambiar estado
    equipos[equipo]["disponible"] = True

    print("Equipo devuelto correctamente.")



def ver_historial():

    print("\n===== HISTORIAL DE PRÉSTAMOS =====")

    for nombre, datos in equipos.items():

        print(f"\nEquipo: {nombre}")

        # Verificar si hay préstamos
        if len(datos["prestamos"]) == 0:
            print("Sin préstamos registrados.")

        else:
            for prestamo in datos["prestamos"]:

                usuario = prestamo[0]
                fecha = prestamo[1]

                print(f"Usuario: {usuario} | Fecha: {fecha}")



def agregar_equipo():

    nuevo_equipo = input("\nIngrese el nombre del nuevo equipo: ")

    # Verificar si ya existe
    if nuevo_equipo in equipos:
        print("Ese equipo ya existe en el sistema.")
        return

    # Agregar equipo al diccionario
    equipos[nuevo_equipo] = {
        "disponible": True,
        "prestamos": []
    }

    print("Equipo agregado correctamente.")



def menu():

    while True:

        print("\nMENU")
        print("1. Ver equipos disponibles")
        print("2. Registrar prestamo")
        print("3. Devolver equipo")
        print("4. Ver historial de prestamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        # Opciones del menú
        if opcion == "1":
            mostrar_equipos()

        elif opcion == "2":
            registrar_prestamo()

        elif opcion == "3":
            devolver_equipo()

        elif opcion == "4":
            ver_historial()

        elif opcion == "5":
            agregar_equipo()

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


menu()