print("Actividad 07")
opcion = 0
estudiantes = {}

while opcion != 4:
    print("\n++ Menú ++")
    print("1. Registrar estudiantes")
    print("2. Mostrar todos los estudiantes y sus cursos")
    print("3. Buscar estudiante por carnet")
    print("4. Salir")

    try:
        opcion = int(input("Ingrese su opción: "))
    except ValueError:
        print("Ingrese una opción válida...")
        continue

    match opcion:
        case 1:
            print("Registrar estudiantes... ")
            cantidad = int(input("Ingrese la cantidad de estudiantes: "))

            for i in range(cantidad):
                print(f"\nEstudiante #{i + 1}")
                while True:
                    carnet = input("Ingrese el carnet del estudiante: ")
                    if carnet in estudiantes:
                        print("El carnet ya fue registrado, ingrese uno nuevo...")
                    else:
                        break

                nombre = input("Ingrese el nombre del estudiante: ")
                edad = int(input("Ingrese la edad del estudiante: "))
                carrera = input("Ingrese la carrera del estudiante: ")

                cursos = {}
                cantidad_cursos = int(input("Ingrese la cantidad de cursos: "))

                for j in range(cantidad_cursos):
                    print(f"\nCurso #{j + 1}")
                    while True:
                        codigo_curso = input("Ingrese el código del curso: ")
                        if codigo_curso in cursos:
                            print("Este código ya está registrado, intentelo de nuevo...")
                        else:
                            break

                    nombre_curso = input("Ingrese el nombre del curso: ")

                    while True:
                        nota_tareas = int(input("Ingrese la nota de tareas: "))
                        if 0 <= nota_tareas <= 100:
                            break
                        else:
                            print("La nota debe estar entre 0 y 100.")

                    while True:
                        nota_parciales = int(input("Ingrese la nota de parciales: "))
                        if 0 <= nota_parciales <= 100:
                            break
                        else:
                            print("La nota debe estar entre 0 y 100.")

                    while True:
                        nota_proyecto = int(input("Ingrese la nota del proyecto: "))
                        if 0 <= nota_proyecto <= 100:
                            break
                        else:
                            print("La nota debe estar entre 0 y 100.")

                    cursos[codigo_curso] = {
                        "nombre_curso": nombre_curso,
                        "nota_tareas": nota_tareas,
                        "nota_parciales": nota_parciales,
                        "nota_proyecto": nota_proyecto
                    }

                estudiantes[carnet] = {
                    "nombre": nombre,
                    "edad": edad,
                    "carrera": carrera,
                    "cursos": cursos
                }
                print(f"\nEstiante {nombre} registrado correctamente...")
        case 2:
            print("++Listado completo de estudiantes++")
            if len(estudiantes) == 0:
                print("No hay estudiantes registrados")
            else:
                for carnet, data in estudiantes.items():
                    print(f"Carnet: {carnet}")
                    print(f"Nombre: {data['nombre']}")
                    print(f"Edad: {data['edad']}")
                    print(f"Carrera: {data['carrera']}")
                    print("\nCursos")
                    for codigo_curso, info in data["cursos"].items():
                        print(f"\nCodigo del curo: {codigo_curso}")
                        print(f"Nombre del curso: {info['nombre_curso']}")
                        print(f"Nota tareas: {info['nota_tareas']}")
                        print(f"Nota parciales: {info['nota_parciales']}")
                        print(f"Nota proyecto: {info['nota_proyecto']}")
        case 3:
            print("Buscar estudiante por carnet... ")
            busco = input("Ingrese el carnet que desea buscar: ")
            if busco in estudiantes:
                data = estudiantes[busco]
                print(f"\nCarent: {busco}")
                print(f"Nombre: {data['nombre']}")
                print(f"Edad: {data['edad']}")
                print(f"Carrera: {data['carrera']}")
                print(f"\nCursos")
                for codigo_curso, info in data["cursos"].items():
                    print(f"Codigo del curso: {codigo_curso}")
                    print(f"Nombre del curso: {info['nombre_curso']}")
                    print(f"Nota tareas: {info['nota_tareas']}")
                    print(f"Nota parciales: {info['nota_parciales']}")
                    print(f"Nota proyecto: {info['nota_proyecto']}")
            else:
                print("El carnet ingresado no existe... ")
