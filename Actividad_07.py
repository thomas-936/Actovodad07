print("Actividad 07")
opcion = 0
estudiantes = {}

while opcion!= 4:
    print("\n++Menu++")
    print("1. Registrar estudiantes: ")
    print("2. Mostrar todos los estidiantes y sus cursos: ")
    print("3. Buscar estudiante por carnet: ")
    print("4. Salir")

    try:
        opcion = int(input("Ingrese su opción: "))
    except ValueError:
        print("Ingrese una opcion valida...")
        continue

    match opcion:
        case 1:


            print("Registrar estudiantes... ")
            cantidad = int(input("Ingrese la cantidad de estudiantes que desea ingresar: "))
            for i in range(cantidad):
                print(f"\nIngrese estudiante #{i+1}")
                while True:
                    carnet = input("Ingrese el carnet del estudiante: ")
                    if carnet in estudiantes:
                        print("El carnet ya fue registrado, ingrese uno nuevo... ")
                    else:
                        break
                nombre = input("Ingrese el nombre del estudiante: ")
                edad = int(input("Ingrese la edad del estudiante: "))
                carrera = input("Ingrese la carrera del estudiante: ")

                cursos= {}
                cantidad_cursos = int(input("Ingrese la cantidad de cursos: "))
                for j in range(cantidad_cursos):
                    print(f"Ingrese el curso #{j+1}: ")
                    while True:
                        codigo_curso = input("Ingrese el codigo del curso: ")
                        if codigo_curso in estudiantes:
                            print("Este codigo ya esta registrado, intentelo de nuevo... ")
                        else :
                            break

                nombre_curso=  input("Ingrese el nombre del curso: ")
                nota_tareas = int(input("Ingrese la nota de las tareas: "))
                if 0<= nota_tareas <= 100:
                    break
                else:
                    print("La nota debe estar entre 0 y 100.")
                nota_parciales = int(input("Ingrese la nota de los parciales: "))
                if 0<= nota_parciales <= 100:
                    break
                else:
                    print("La nota debe estar entre 0 y 100.")
                nota_proyecto = int(input("Ingrese la nota del proyecto: "))
                if 0 <= nota_proyecto <= 100:
                    break
                else:
                    print("La nota debe estar entre 0 y 100.")

                cursos[cantidad_cursos]= {

                }
