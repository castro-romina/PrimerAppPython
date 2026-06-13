import tkinter as tk;

def saludar():
    nombre = entrada.get()
    etiqueta_resultado.config(text=f"¡Hola, {nombre}!")

ventana = tk.Tk()
ventana.config(width=400, height=300, bg="lightblue")
ventana.title("Mi primer app de escritorio")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingresá tu nombre:", bg="lightblue")
etiqueta.pack(pady=10)

# Campo de texto
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Botón
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=10)

# Etiqueta de resultado
etiqueta_resultado = tk.Label(ventana, text="", bg="lightblue", font=("Arial", 14))
etiqueta_resultado.pack(pady=10)

ventana.mainloop()
