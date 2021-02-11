from tkinter import*
from tkinter import messagebox

from modulo_pantallas import*

root = Tk()
root.title("Primera Aplicacion")
root.geometry("600x800")

# Instancia de la clase pantalla para crear la pantalla de inicio de mi aplicacion
aplicacion = pantalla_inicio(root)
aplicacion.mainloop()
