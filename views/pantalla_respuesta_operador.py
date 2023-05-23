import tkinter as tk


class PantallaRespuestaOperador(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.ventana_ancho = 800
        self.ventana_alto = 600

        self.title("Pantalla Respuesta del Operador")
        self.geometry(self.centrar_ventana(self.ventana_ancho, self.ventana_alto))
        self.init_ui()
    
    def centrar_ventana(self, ventana_ancho, ventana_alto):
        ventana_x = self.winfo_screenwidth() // 2 - ventana_ancho // 2
        ventana_y = self.winfo_screenheight() // 2 - ventana_alto // 2

        return f'{ventana_ancho}x{ventana_alto}+{ventana_x}+{ventana_y}'

    def init_ui(self):
        pass

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
