from tkinter import Tk
from views.pantalla_respuesta_operador import PantallaRespuestaOperador

def main ():
    ventana = Tk()
    ventana.geometry('800x600')

    pantallaRespuestaOperador = PantallaRespuestaOperador(ventana)
    pantallaRespuestaOperador.mainloop()

if __name__ == '__main__':
    main()