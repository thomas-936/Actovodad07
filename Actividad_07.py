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



