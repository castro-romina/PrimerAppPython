user = input("Ingrese nombre de usuario:")
password = input("Ingrese la contraseña:")

if user != "admin" or password != "uni123":
    print ("Usuario y/o contraseña incorrecta")
else:
    alumnos={}
    while True:
        print ("1- Añadir alumno a la lista.\n 2- Ver la lista de Alumnos.\n3- Salir.\n")
        opcion = int(input("Ingrese el numero de la operacion que deseas ejecutar:"))
        
        if opcion < 1 or opcion > 3:
            print("Opcion incorrecta.\n")
        else:
            if opcion==3:
                print ("¡Gracias por utilizar el programa!")
                break
            else:
                if opcion==1:
                    nombre= input("Ingrese Nombre del alumno:")
                    curso=input("Ingrese la cantidad de cursos:")
                    alumnos[nombre]=curso
                    print ("El alumno fue añadido a la lista!\n")
                else:
                    print ("Lista de alumnos:\n")
                    for nombre, curso in alumnos.items():
                        print (nombre,"-",curso)
            





