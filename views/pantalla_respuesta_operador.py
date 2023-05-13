from tkinter import Frame, Button, Label

class PantallaRespuestaOperador(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.master = master
        self.pack()
        self.init_ui()

    def init_ui(self):
        self.master.title("PantallaRespuestaOperador")
        self.label = Label(self, text="Hola")
        self.label.pack()

        self.button1 = Button(self, text='Aceptar')
        self.button1.pack(side='top')
        
        self.button1 = Button(self, text='Cancelar')
        self.button1.pack(side='top')

    def mostrarDatosLLamada(self):
        pass

    def mostrarNombreValidacion(self):
        pass

    def pedirRespuestaValidacion(self):
        pass

    def tomarRespuestaValidacion(self):
        pass

    def pedirDescripcionRespuesta(self):
        pass

    def tomarDescripcionRespuesta(self):
        pass

    def pedirAccionARealizar(self):
        pass

    def tomarAccionARealizar(self):
        pass

    def pedirConfirmacionDeOperacion(self):
        pass

    def tomarConfirmacionDeOperacion(self):
        pass

    def mostrarMensajeRegistroDeAccion(self):
        pass
