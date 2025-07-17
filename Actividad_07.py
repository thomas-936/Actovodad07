print("Actividad 07")
opcion = 0
estudiantes = {}
while opcion!= 4:
    print("++Menu++")
    print("1. Registrar estudiantes: ")
    print("2. Mostrar todos los estidiantes y sus cursos: ")
    print("3. Buscar estudiante por carnet: ")
    print("4. Salir")
    opcion = int(input("Ingrese su opción: "))

    match opcion:
        case 1:
            print("Registrar estudiantes... ")
            cantidad = int(input("Ingrese la cantidad de estudiantes que desea ingresar: "))
            for i in range(cantidad):
                print(f"\nIngrese estudiante #{i}")
                while True:
                    carnet = input("Ingrese el carnet del estudiante: ")
                    if carnet in estudiantes:
                        print("El carnet ya fue registrado, ingrese uno nuevo... ")
                    else:
                        break
            nombre = input("Imngrese el nombre del estudiante: ")
            edad = int(input("Ingrese la edad del estudiante: "))
            carrera = input("Ingrese la carrera del estudiante: ")
            cantidad_cursos = int(input("Ingrese la cantidad de cursoso: "))
            for j in range(cantidad_cursos):
                print(f"Ingrese el curso #{j}: ")
                while True:
                    codigo_curso = input("Ingrese el codigo del curso: ")
                    if codigo_curso in estudiantes:
                        print("Este codigo ya esta registrado, intentelo de nuevo... ")
                    else :
                        break
            nota_tareas = int(input("Ingrese la nota de las tareas: "))
            if nota_tareas > 0 and nota_tareas < 100:
                print("Nota ingresada...")
            else:
                print("Ingrese una nota correcta.")
            nota_parciales = int(input("Ingrese la nota de los parciales: "))
            if nota_parciales > 0 and nota_parciales < 100:
                print("Nota ingresada... ")
            else:
                print("Ingrese una nota correcta.")
            nota_proyecto = int(input("Ingrese la nota del proyecto: "))
            if nota_proyecto > 0 and nota_proyecto < 100:
                print("Nota ingresada...")
            else:
                print("Ingrese una nota correcta.")




