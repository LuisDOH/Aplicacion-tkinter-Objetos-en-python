'''
    ==================================================
        Este modulo contiene a todas las clases
        'logicas' de mi programa
        (Ej:Registro, persona, alumno, empleado)
    ==================================================
'''
class Registro():
    def __init__(self, nombre, edad, clave):
        self.nombre_usuario = nombre
        self.edad = edad
        self.clave = clave

    def informacion(self):
        print("Nombre: %s\nEdad: %s\nClave: %s" %(self.nombre_usuario, self.edad, self.clave))
