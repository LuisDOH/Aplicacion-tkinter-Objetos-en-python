from tkinter import*
from tkinter import messagebox

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
        self.btn_ingreso = Button(self, text = "Login", bg = "#45b39d", fg = "white", font = ("Corbel",17))
        self.btn_ingreso.place(relwidth = 0.5, relx = 0.25, rely = 0.7)


        # Boton para ir a pantalla principal
        self.btn_menu = Button(self, text = "Menu principal", font = ("arial",12), command = lambda: self.ir_a_menu(master))
        self.btn_menu.place(relx = 0.1, rely = 0.1)

    # Metodo para ir a la pantalla principal
    def ir_a_menu(self, padre):
        self.destroy()
        p_inicio = pantalla_inicio(padre)

    def ingresar(self):
        # Capturamos datos de las cajas de texto
        user = self.txt_nombre.get()
        pwd = self.txt_clave.get()

        try:
            # Si el archivo existe
            archivo_externo = open(r"/home/lolguin/Desktop/Backend/Pre/Tkinter/AplicacionV_1/registros.txt","r+")
            # Realizo alguna operacion
            # Generar un vector con los datos del archivo txt
            data = archivo_externo.readlines() # data = ["",""]
            archivo_externo.close()
            print(data)

        except:
            print("No existe el archivo que deseas abrir")
            archivo_externo = open(r"/home/lolguin/Desktop/Backend/Pre/Tkinter/AplicacionV_1/registros.txt","a+")
            # Realizo alguna operacion
            # Generar un vector vacio
            data = []
            archivo_externo.close()

        # Bandera que indique si el usuario y la clave son correctos
        datos_correctos = False

        for registro in data:
            #registro = "user , 27 , clave\n"
            [usuario_r, edad_r, clave_r] = registro.split(",")
            # Quitamos \n de la clave
            clave_r = clave_r.strip("\n")

            # Verificar si el usuario y la clave son correctos
            if user == usuario_r and pwd == clave_r:
                datos_correctos = True
                break

        if datos_correctos == True:
            messagebox.showwarning(message = "Bienvenido al sistema", title = "Bienvenida")
        else:
            messagebox.showwarning(message = "El usuario o la clave no son correctos", title = "Error")

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
        print(nombre_usuario)

        # Revisar si tenemos un archivo externo para guardar nuestros datos
        #archivo_externo = open(r"/home/lolguin/Desktop/Backend/Pre/Tkinter/AplicacionV_1/registros.txt","a+")
        # Realizo alguna operacion
        #archivo_externo.close()

        #archivo_externo = open(r"/home/lolguin/Desktop/Backend/Pre/Tkinter/AplicacionV_1/registros.txt","r+")
        # Realizo alguna operacion
        #archivo_externo.close()

        # Control de excepciones
        try:
            # Si el archivo existe
            archivo_externo = open(r"/home/lolguin/Desktop/Backend/Pre/Tkinter/AplicacionV_1/registros.txt","r+")
            # Realizo alguna operacion
            # Generar un vector con los datos del archivo txt
            data = archivo_externo.readlines() # data = ["",""]
            archivo_externo.close()
            print(data)

        except:
            print("No existe el archivo que deseas abrir")
            archivo_externo = open(r"/home/lolguin/Desktop/Backend/Pre/Tkinter/AplicacionV_1/registros.txt","a+")
            # Realizo alguna operacion
            # Generar un vector vacio
            data = []
            archivo_externo.close()

        # Verificar si el usuario ya existe
        # Bandera
        existe_usuario = False

        # Recorrer todos los elementos del arreglo data (la informacion que contiene el archivo txt)
        #data = ["user,27,clave\n","user1,30,clave1\n","user2,30,clave2\n"]

        for registro in data:
            #registro = "user , 27 , clave\n"
            [usuario_r, edad_r, clave_r] = registro.split(",")
            # Quitamos \n de la clave
            clave_r = clave_r.strip("\n")

            # Verificar si el usuario a registrar ya existe
            if nombre_usuario == usuario_r:
                existe_usuario = True
                break


        # registrar al usuario nuevo(en caso de que el usuario no exista)
        if existe_usuario == False:
            archivo_externo = open(r"/home/lolguin/Desktop/Backend/Pre/Tkinter/AplicacionV_1/registros.txt","a+")
            archivo_externo.write("%s,%s,%s\n" %(nombre_usuario,edad_usuario,clave_usuario))
            archivo_externo.close()
        else:
            messagebox.showwarning(message = "El usuario a registrar ya existe", title = "Alerta")


# Creamos la raiz o base de la apliacion
root = Tk()
root.title("Primera Aplicacion")
root.geometry("600x800")

# Instancia de la clase pantalla para crear la pantalla de inicio de mi aplicacion
aplicacion = pantalla_inicio(root)
aplicacion.mainloop()
