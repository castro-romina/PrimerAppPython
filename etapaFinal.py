import tkinter as tk

user = input("Ingrese nombre de usuario:")
password = input("Ingrese la contraseña:")

if user != "admin" or password != "uni123":
    print("Usuario y/o contraseña incorrecta")
else:
    alumnos = {}

def agregar_alumno():
    nombre = entrada_nombre.get()
    curso = entrada_curso.get()
    alumnos[nombre] = curso
    print("El alumno fue añadido a la lista!\n")

def ver_lista():
    print("Lista de alumnos:")
    for nombre, curso in alumnos.items():
        print(nombre, "-", curso)
    print()

def ver_cantidad_cursos():
    nombre = entrada_nombre.get()
    if nombre in alumnos:
        print(f"{nombre} tiene {alumnos[nombre]} cursos.\n")
    else:
        print("Alumno no encontrado.\n")

ventana = tk.Tk()
ventana.title("Proyecto integrador")
ventana.config(width=600, height=600)

tk.Button(ventana, text="Ver lista de alumnos", command=ver_lista).pack(pady=10, padx=10, anchor="w")

frame_nombre = tk.Frame(ventana)
frame_nombre.pack(pady=5, padx=10, anchor="w")
tk.Label(frame_nombre, text="Nombre alumno:").pack(side="left")
entrada_nombre = tk.Entry(frame_nombre)
entrada_nombre.pack(side="left", padx=5)

frame_curso = tk.Frame(ventana)
frame_curso.pack(pady=5, padx=10, anchor="w")
tk.Label(frame_curso, text="Cursos:").pack(side="left")
entrada_curso = tk.Entry(frame_curso, width=10)
entrada_curso.pack(side="left", padx=5)

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10, padx=10, anchor="w")
tk.Button(frame_botones, text="Agregar a la lista", command=agregar_alumno).pack(side="left", padx=5)
tk.Button(frame_botones, text="Ver cantidad de cursos", command=ver_cantidad_cursos).pack(side="left", padx=5)

ventana.mainloop()