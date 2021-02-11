'''
    ================================================
        Este modulo contiene todas las clases
        para la interfaz visual del programa
    =================================================
'''
from tkinter import*
from tkinter import messagebox

from modulo_clases_logicas import*
import pickle

class Pantalla(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(width = 500, height = 700)


        self.btn_salir = Button(self, text = "Cerrar", font = ("Arial", 20))
        self.btn_salir.config(command = lambda:self.cerrar_aplicacion(master))
        self.btn_salir.place(relx = 0.80, rely = 0.9)

        # Montamos el contenedor (pantalla)
        self.pack()

    # Metodo de la super clase para cerrar
    def cerrar_aplicacion(self, padre):
        padre.destroy()

class pantalla_inicio(Pantalla):
    def __init__(self, master):
        super().__init__(master)

        # Titulo de la pantalla
        self.lbl_titulo = Label(self, text = "Bienvenido al sistema",font = ("Arial", 30))
        self.lbl_titulo.place(relx = 0.15, rely = 0.1)

        # Boton de ingreso
        self.btn_login = Button(self, text="Ingresar", bg="gold", command = lambda:self.cambio_a_ingreso(master))
        self.btn_login.config(font = ("arial",16))
        self.btn_login.place(relx = 0.1, rely = 0.5, relwidth = 0.3)

        # Boton de registro
        self.btn_registrar = Button(self, text="Registrar", bg="gold", command = lambda:self.cambio_a_registro(master))
        self.btn_registrar.config(font = ("arial",16))
        self.btn_registrar.place(relx = 0.6, rely = 0.5, relwidth = 0.3)

    # Funcion para cambiar a la pantalla de inicio de sesion
    def cambio_a_ingreso(self, padre):
        self.destroy()
        login = pantalla_ingreso(padre)

    # Funcion para cambiar a la pantalla de inicio de registro
    def cambio_a_registro(self, padre):
        self.destroy()
        registro = pantalla_registro(padre)

class pantalla_ingreso(Pantalla):
    def __init__(self, master):
        super().__init__(master)

        # Titulo de la pantalla
        self.mensaje = Label(self, text = "Bienvenido ingrese sus datos", font = ("Corbel",17), fg = "#2c3e50")
        self.mensaje.place(relx = 0.25, rely = 0.3)

        # Etiquetas(titulos para los espacios de usuario y clave)
        self.lbl_usuario = Label(self, text = "Usuario", font = ("Corbel", 16), fg = "#2980b9")
        self.lbl_usuario.place(relx = 0.42, rely = 0.4)
        self.lbl_clave = Label(self, text = "Clave", font = ("Corbel", 16), fg = "#2980b9")
        self.lbl_clave.place(relx = 0.44, rely = 0.55)

        # Cajas de texto para ingresar los datos
        self.txt_nombre = Entry(self, font = ("Corbel", 15), bg = "white", justify = "center")
        self.txt_nombre.place(relx = 0.25, rely = 0.45, relwidth = 0.5)
        self.txt_clave = Entry(self, font = ("Corbel", 15), bg = "white", justify = "center", show = "*")
        self.txt_clave.place(relx = 0.25, rely = 0.6, relwidth = 0.5)

        # Boton para inicio de sesion
        self.btn_ingreso = Button(self, text = "Login", bg = "#45b39d", fg = "white", font = ("Corbel",17),command = lambda: self.ingresar(master))
        self.btn_ingreso.place(relwidth = 0.5, relx = 0.25, rely = 0.7)


        # Boton para ir a pantalla de principal
        self.btn_menu = Button(self, text = "Menu principal", font = ("arial",12), command = lambda: self.ir_a_menu(master))
        self.btn_menu.place(relx = 0.1, rely = 0.1)

    # Metodo para ir a la pantalla principal
    def ir_a_menu(self, padre):
        self.destroy()
        p_inicio = pantalla_inicio(padre)

     # Metodo para ingresar con usuario y clave
    def ingresar(self, padre):
        nombre_usuario = self.txt_nombre.get()
        clave_usuario = self.txt_clave.get()

        self.txt_nombre.delete(0,END)
        self.txt_clave.delete(0,END)

        self.txt_nombre.focus()
        print(nombre_usuario)

        # Verificamos si el archivo existe, si no lo creamos
        try:
            # ---------- Si el archivo existe recatamos la informacion que esta dentro---------
            data = open(r"/home/lolguin/Desktop/Backend/Python/Aplicacion_modular_V1/Datos","rb")
            lista_registros = pickle.load(data)
            data.close()

        except:
            # --------- Si no exitse entonces creamos un archivo nuevo y dejamos nuestra lista como vacia
            data = open(r"/home/lolguin/Desktop/Backend/Python/Aplicacion_modular_V1/Datos","wb")
            data.close()
            print("==== Se ha creado un nuevo archivo =====")
            lista_registros = []


        # Crear una bandera que indique si encuentra una coincidencia
        usuario_correcto = False
        clave_correcta = False
        for registro in lista_registros:
            # El dato nombre que viene del formulario y el atributo nombre que esta en los objetos
            if nombre_usuario == registro.nombre_usuario:
                if clave_usuario == registro.clave:
                    usuario_correcto = True
                    clave_correcta = True
                    break
                else:
                    usuario_correcto = True
                    clave_correcta = False
                    break

        # Verificar cuales banderas estan True para indicar un mensaje
        if usuario_correcto == True and clave_correcta == True:
            messagebox.showinfo(message = f"Bienvenido al sistema {nombre_usuario}", title = "Bienvenido")

            # Ingresamos a nuestra pantalla de bienvenida
            self.destroy()
            bienvenida = pantalla_bienvenida(padre)

        elif usuario_correcto == True and clave_correcta == False:
            messagebox.showwarning(message = "La clave es incorrecta", title = "Alerta")
        else:
            messagebox.showwarning(message = f"El usuario: {nombre_usuario} no esta registrado", title = "Alerta")

        # Liberamos el espacio de la lista registros
        del(lista_registros)

class pantalla_registro(Pantalla):
    def __init__(self,master):
        super().__init__(master)

        # Etiqueta pra el titulo de la pagina
        self.mensaje = Label(self, text = "Registrate", font = ("Corbel",20), fg = "#dc7633")
        self.mensaje.place(relx = 0.4, rely = 0.3)

        # Etiquetas(titulos para los datos del usuario)
        self.nombre = Label(self, text="Nombre",font = ("Corbel", 16), fg = "#196f3d")
        self.nombre .place(relx = 0.2, rely = 0.4)
        self.edad = Label(self, text="Edad",font = ("Corbel", 16), fg = "#196f3d")
        self.edad.place(relx = 0.2, rely = 0.45)
        self.clave = Label(self, text="Clave",font = ("Corbel", 16), fg = "#196f3d")
        self.clave.place(relx = 0.2, rely = 0.5)

        self.txt_nombre = Entry(self,font = ("Corbel", 16), bg = "white")
        self.txt_nombre.place(relx = 0.45, rely = 0.4)
        self.txt_edad = Entry(self,font = ("Corbel", 16), bg = "white")
        self.txt_edad.place(relx = 0.45, rely = 0.45)
        self.txt_clave = Entry(self,font = ("Corbel", 16), bg = "white")
        self.txt_clave.place(relx = 0.45, rely = 0.5)

        # Boton para crear nuevo registro
        self.btn_registro = Button(self, text="Crear registro", font = ("Corbel", 14), command = self.registrar)
        self.btn_registro.place(relx = 0.7, rely = 0.6)

        # Boton para ir a pantalla de principal
        self.btn_menu = Button(self, text = "Menu principal", font = ("arial",12), command = lambda: self.ir_a_menu(master))
        self.btn_menu.place(relx = 0.1, rely = 0.1)


    # Metodo para ir a la pantalla principal
    def ir_a_menu(self, padre):
        self.destroy()
        p_inicio = pantalla_inicio(padre)

    # Metodo para crear un nuevo resgistro
    def registrar(self):
        nombre_usuario = self.txt_nombre.get()
        edad_usuario = self.txt_edad.get()
        clave_usuario = self.txt_clave.get()

        self.txt_nombre.delete(0,END)
        self.txt_edad.delete(0,END)
        self.txt_clave.delete(0,END)

        self.txt_nombre.focus()


        '''
        ====================================================================================
        1- Verificacion la existencia de un archivo donde estan guardados los usuarios
        2- Creamos un objeto de tipo registro con la informacion capturada
            en el formulario y lo anexamos a la lista re usuarios
        3- Abrimos un enlace para guardar la lista de usuarios actualizada y volcamos
            la informacion

        * Recordar:
             wb => write binary;    rb => read binary
        =====================================================================================
        '''
        # Verificamos si el archivo existe, si no lo creamos
        try:
            # ---------- Si el archivo existe recatamos la informacion que esta dentro---------
            data = open(r"/home/lolguin/Desktop/Backend/Python/Aplicacion_modular_V1/Datos","rb")
            lista_registros = pickle.load(data)
            data.close()

        except:
            # --------- Si no exitse entonces creamos un archivo nuevo y dejamos nuestra lista como vacia
            data = open(r"/home/lolguin/Desktop/Backend/Python/Aplicacion_modular_V1/Datos","wb")
            data.close()
            print("==== Se ha creado un nuevo archivo =====")
            lista_registros = []


        # Crear una bandera que indique si encuentra una coincidencia
        existe_usuario = False
        for registro in lista_registros:
            # El dato nombre que viene del formulario y el atributo nombre que esta en los objetos
            if nombre_usuario == registro.nombre_usuario:
                existe_usuario = True
                break

        if existe_usuario == True:
            messagebox.showwarning(message= "Usuario ya existe", title="Alerta")
        else:
            # Creamos el registro con la informacion del nuevo usuario
            registro = Registro(nombre_usuario, edad_usuario, clave_usuario)

            # Agregamos el registro a la lista
            lista_registros.append(registro)
            print(len(lista_registros))


            # Volcamos la lista actualizada en el archivo binario
            data  = open(r"/home/lolguin/Desktop/Backend/Python/Aplicacion_modular_V1/Datos","wb")
            pickle.dump(lista_registros,data)
            data.close()
            messagebox.showwarning(message = "Registro exitoso", title = "Aviso")


'''
    ==============================================================================
        Primer pantalla dentro de la aplicacion que mostrara todos los usuarios
        registrados en nuestra base de datos
    ==============================================================================
'''

class pantalla_bienvenida(Pantalla):
    def __init__(self, master):
        super().__init__(master)
        self.titulo = Label(self, text = "Usuarios Registrados", font = ("Corbel",18),fg = "#45b39d", justify="center")
        self.titulo.place(relwidth = 0.5, relx = 0.25, rely = 0.1)

        self.lbl_nombre = Label(self, text = "Nombre usuario:", font = ("Corbel",14), fg = "red",justify="center")
        self.lbl_nombre.place(relwidth = 0.4, relx = 0.1, rely = 0.3)

        self.lbl_edad= Label(self, text = "Edad:", font = ("Corbel",14),  fg = "red", justify="center")
        self.lbl_edad.place(relwidth = 0.2, relx = 0.5, rely = 0.3)

        self.lbl_clave= Label(self, text = "Clave:", font = ("Corbel",14), fg = "red", justify="center")
        self.lbl_clave.place(relwidth = 0.2, relx = 0.8, rely = 0.3)

        data = open(r"/home/lolguin/Desktop/Backend/Python/Aplicacion_modular_V1/Datos","rb")
        lista_registros = pickle.load(data)
        data.close()

        iter = 0.1
        for registro in lista_registros:
            label = Label(self, text = f"{registro.nombre_usuario}", font = ("Corbel",12), justify="center")
            label.place(relwidth = 0.4, relx = 0.1, rely =(0.3 + iter))

            label = Label(self, text = f"{registro.edad}", font = ("Corbel",12), justify="center")
            label.place(relwidth = 0.2, relx = 0.5, rely = (0.3 + iter))

            label = Label(self, text = f"{registro.clave}", font = ("Corbel",12), justify="center")
            label.place(relwidth = 0.2, relx = 0.8, rely = (0.3 + iter))

            iter += 0.1
