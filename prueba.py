import tkinter as tk
from tkinter import messagebox

def solo_numeros(char):
    return char.isdigit()

def validar_input(*args):
    entrada = entry.get()
    if not entrada.isdigit():
        messagebox.showwarning("Error", "Por favor, ingrese solo números.")
        entry.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Solo Números")

# Crear el Entry con la validación
validacion = ventana.register(solo_numeros)
entry = tk.Entry(ventana, validate="key", validatecommand=(validacion, '%S'))
entry.pack(padx=10, pady=10)

# Configurar la función de validación
entry.bind("<FocusOut>", validar_input)

# Ejecutar la aplicación
ventana.mainloop()