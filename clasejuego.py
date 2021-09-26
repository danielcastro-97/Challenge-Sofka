import random
from datetime import date
from tkinter import *


class PlayColombia:
    def __init__(self):
        self.__categoria = 1
        self.__nombre = "Jugador"
        self.__puntaje = 0
        self.__bandera = 0  # Representa la opción escogida por el usuario
        self.interfaz = Tk()

    def nuevoJugador(self, nombre):
        print("Nombre de jugador guardado")
        self.__nombre = nombre
        print("jugador: ", self.__nombre)
        self.cerrarJuego()
        self.jugarRonda()

    def cerrarJuego(self):
        self.interfaz.destroy()

    def imgRonda(self):
        if self.__categoria == 1:
            num = "1.png"
            mC = "0.png"
            mD = "0.png"
            mU = "0.png"
        elif self.__categoria == 2:
            num = "2.png"
            mC = "0.png"
            mD = "1.png"
            mU = "0.png"
        elif self.__categoria == 3:
            num = "3.png"
            mC = "0.png"
            mD = "3.png"
            mU = "0.png"
        elif self.__categoria == 4:
            num = "4.png"
            mC = "0.png"
            mD = "6.png"
            mU = "0.png"
        elif self.__categoria == 5:
            num = "5.png"
            mC = "1.png"
            mD = "0.png"
            mU = "0.png"
        # file = "iconos/num1.png"
        # file="iconos/pun1.png"
        ronda = "iconos/num" + num
        numC = "iconos/pun" + mC
        numD = "iconos/pun" + mD
        numU = "iconos/pun" + mU

        return ronda, numU, numD, numC

    def puntosRonda(self):
        if self.__categoria == 1:
            val = 10
        elif self.__categoria == 2:
            val = 20
        elif self.__categoria == 3:
            val = 30
        elif self.__categoria == 4:
            val = 40
        elif self.__categoria == 5:
            val = 100

        texto = "Por " + str(val) + " puntos"
        return texto

    def cargarPreguntas(self):
        aleatorio = int(random.uniform(1, 6))
        ruta = "preguntas/cat" + str(self.__categoria) + "pre" + str(aleatorio) + ".txt"
        fichero = open(ruta, 'r', encoding="utf8")
        pregunta = fichero.readline()
        opcion1 = fichero.readline()
        opcion2 = fichero.readline()
        opcion3 = fichero.readline()
        opcion4 = fichero.readline()
        respuesta = fichero.readline()
        mensaje = fichero.readline()
        fichero.close()
        return pregunta, opcion1, opcion2, opcion3, opcion4, respuesta, mensaje

    def pasarNivel(self):
        if self.__categoria < 5:
            self.__categoria += 1
            self.jugarRonda()
        else:
            self.guardarHistorico()

    def leerHistoricos(self):
        hist = open('historicos/historicosColombia.txt', 'r', encoding="utf8")
        historicos = hist.read()
        hist.close()
        return historicos

    def guardarHistorico(self):
        # Los datos historicos se guardan en un archivo txt
        hist = open('historicos/historicosColombia.txt', 'r', encoding="utf8")

        # Se crea una lista vacia para contener los datos de los jugadores
        listajugadores = []
        for linea in hist:
            jugador = list(map(str, linea.split(' ')))  # se covierte a lista los datos de cada linea
            jugador[1] = int(jugador[1])  # El dato de puntaje se convierte a entero para poder operarlo
            listajugadores.append(jugador)
        hist.close()

        jugadorAct = [self.__nombre, self.__puntaje, str(date.today()) + "\n"]
        listajugadores.append(jugadorAct)  # Se inserta el puntaje y los datos del jugador actual a la lista

        # JugadoresOrd contiene a los 11 datos ordenados del mayor al menor puntaje
        jugadoresOrd = sorted(listajugadores, key=lambda puntaje: puntaje[1], reverse=True)
        jugadoresOrd.pop()  # Se elimina al jugador de la última posición

        # Se convierte a texto de nuevo la lista con los jugaores ordenados
        texto = ""
        for i in jugadoresOrd:
            texto += " ".join([str(_) for _ in i])
        nHistorial = open("historicos/historicosColombia.txt", 'w', encoding="utf8")
        nHistorial.write(str(texto))
        nHistorial.close()

    def sumarPuntos(self):
        if self.__categoria == 1:
            self.__puntaje += 10
        elif self.__categoria == 2:
            self.__puntaje += 20
        elif self.__categoria == 3:
            self.__puntaje += 30
        elif self.__categoria == 4:
            self.__puntaje += 40
        elif self.__categoria == 5:
            self.__puntaje += 100
        print("puntos acumulados: ", self.__puntaje, "\n")

        self.pasarNivel()

    def validarResultados(self, respuesta, opcion):
        if respuesta == opcion:
            print("---------Respuesta Correcta-----------")
            self.sumarPuntos()
        else:
            print("Respuesta incorrecta\nJuego terminado")
            self.terminarJuego()

    def terminarJuego(self):
        self.guardarHistorico()

    def lanzarJuego(self):
        self.interfaz.title("¿Quién es un buen colombiano?")
        self.interfaz.iconbitmap("iconos/ColB.ico")
        self.interfaz.geometry("600x610")
        self.interfaz.config(bg="white")

        miFrame1 = Frame(self.interfaz)
        miFrame1.config(bg="yellow", width="550", height="300", cursor="hand2")
        miFrame1.pack(side="top", anchor="s")

        miFrame2 = Frame()
        miFrame2.config(bg="blue", width="550", height="150", cursor="hand2")
        miFrame2.pack(side="top", anchor="s")

        miFrame3 = Frame()
        miFrame3.config(bg="red", width="550", height="150", cursor="hand2")
        miFrame3.pack(side="top", anchor="s")

        miFrame4 = Frame()
        miFrame4.config(width="550", height="50")
        miFrame4.pack(side="top", anchor="s")

        miLabel1 = Label(miFrame1, text="¡Bienvenido a!", font=("Comic Sans MS", 20))
        miLabel1.config(bg="yellow")
        miLabel1.grid(row=0, column=0)

        miLabel2 = Label(miFrame1, text="¿Quién es un \nbuen colombiano?", font=("Comic Sans MS", 50))
        miLabel2.config(bg="yellow")
        miLabel2.grid(row=1, column=0)

        miLabel3 = Label(miFrame2, text="¿Te consideras bueno en \ncultura geneal colombiana?",
                         font=("Comic Sans MS", 30))
        miLabel3.config(bg="blue")
        miLabel3.grid(row=0, column=0)

        miLabel4 = Label(miFrame3, text="Ingresa tu nombre \npara empezar", font=("Comic Sans MS", 20))
        miLabel4.config(bg="red")
        miLabel4.grid(row=0, column=0)

        nombreJugador = StringVar()
        cuadroNombre = Entry(miFrame3, textvariable=nombreJugador)
        cuadroNombre.insert(0, "Jugador")
        cuadroNombre.grid(row=1, column=0, padx=10, pady=10)

        botonEnvio = Button(miFrame4, text="Enviar", command=lambda: self.nuevoJugador(nombreJugador.get()))
        botonEnvio.grid(row=0, column=0, padx=10, pady=10)

        botonSalir = Button(miFrame4, text="Salir", command=lambda: self.cerrarJuego())
        botonSalir.grid(row=0, column=1, padx=10, pady=10)

        self.interfaz.mainloop()

    def jugarRonda(self):
        juego = Tk()
        juego.title("¿Quién es un buen colombiano?")
        juego.iconbitmap("iconos/ColB.ico")
        miFrame1 = Frame(juego)
        miFrame1.config(width="1000", height="600")
        miFrame1.pack()

        miFrame2 = Frame(miFrame1)
        miFrame2.config(width="100", height="400")
        miFrame2.grid(row=0, column=0)

        miFrame3 = Frame(miFrame1)
        miFrame3.config(width="900", height="600")
        miFrame3.grid(row=0, column=1)

        miFrame9 = Frame(miFrame3)
        miFrame9.config(width="500", height="100")
        miFrame9.grid(row=0, column=0)

        miFrame4 = Frame(miFrame3)
        miFrame4.config(width="500", height="100")
        miFrame4.grid(row=1, column=0)

        miFrame5 = Frame(miFrame3)
        miFrame5.config(width="500", height="100")
        miFrame5.grid(row=2, column=0)

        miFrame6 = Frame(miFrame3)
        miFrame6.config(width="1000", height="200")
        miFrame6.grid(row=3, column=0)

        miFrame7 = Frame(miFrame3)
        miFrame7.config(width="500", height="100")
        miFrame7.grid(row=4, column=0)

        miFrame8 = Frame(miFrame3)
        miFrame8.config(width="500", height="100")
        miFrame8.grid(row=5, column=0)

        miLabel1 = Label(miFrame2, text="Ronda", font=("Comic Sans MS", 20))
        miLabel1.grid(row=0, column=0)

        miLabel3 = Label(miFrame9, text="Jugador: ", font=("Comic Sans MS", 20))
        miLabel3.grid(row=0, column=0)

        jugador = StringVar()
        jugador.set(self.__nombre)
        miLabel10 = Label(miFrame9, textvariable=jugador)
        miLabel10.grid(row=0, column=1)

        miLabel4 = Label(miFrame4, text="Puntaje: ", font=("Comic Sans MS", 20))
        miLabel4.grid(row=0, column=0)

        textopuntos = StringVar()
        textopuntos.set(self.puntosRonda())
        milabel5 = Label(miFrame5, textvariable=textopuntos)
        milabel5.grid(row=0, column=0)

        datosh = StringVar()
        datosh.set(self.leerHistoricos())
        miLabel16 = Label(miFrame2, textvariable=datosh)
        miLabel16.grid(row=2, column=0)

        pregunta, opcion1, opcion2, opcion3, opcion4, respuesta, mensaje = self.cargarPreguntas()
        print(pregunta)

        textPregunta = StringVar()
        textPregunta.set(pregunta)
        milabel6 = Label(miFrame6, textvariable=textPregunta)
        milabel6.grid(row=1, column=0)

        RmiImagen, RimgU, RimgD, RimgC = self.imgRonda()

        miImagen = PhotoImage(file=RmiImagen)
        milabel2 = Label(miFrame2, image=miImagen)
        milabel2.grid(row=1, column=0)

        imgU = PhotoImage(file=RimgU)
        milabel7 = Label(miFrame4, image=imgU)
        milabel7.grid(row=0, column=3)

        imgD = PhotoImage(file=RimgD)
        milabel8 = Label(miFrame4, image=imgD)
        milabel8.grid(row=0, column=2)

        imgC = PhotoImage(file=RimgC)
        milabel9 = Label(miFrame4, image=imgC)
        milabel9.grid(row=0, column=1)


        def cambiaColor(num):
            botonA.config(bg="white")
            botonB.config(bg="white")
            botonC.config(bg="white")
            botonD.config(bg="white")

            if num == 1:
                botonA.config(bg="green")
                self.__bandera = 1
            elif num == 2:
                botonB.config(bg="green")
                self.__bandera = 2
            elif num == 3:
                botonC.config(bg="green")
                self.__bandera = 3
            elif num == 4:
                botonD.config(bg="green")
                self.__bandera = 4
            elif num == 0:
                botonA.config(bg="white")
                botonB.config(bg="white")
                botonC.config(bg="white")
                botonD.config(bg="white")
                self.__bandera = 0

        opcA = StringVar()
        opcA.set(opcion1)
        botonA = Button(miFrame7, textvariable=opcA, bg="white", command=lambda: cambiaColor(1))
        botonA.grid(row=0, column=0, padx=10, pady=10)

        opcB = StringVar()
        opcB.set(opcion2)
        botonB = Button(miFrame7, textvariable=opcB, bg="white", command=lambda: cambiaColor(2))
        botonB.grid(row=0, column=1, padx=10, pady=10)

        opcC = StringVar()
        opcC.set(opcion3)
        botonC = Button(miFrame7, textvariable=opcC, bg="white", command=lambda: cambiaColor(3))
        botonC.grid(row=1, column=0, padx=10, pady=10)

        opcD = StringVar()
        opcD.set(opcion4)
        botonD = Button(miFrame7, textvariable=opcD, bg="white", command=lambda: cambiaColor(4))
        botonD.grid(row=1, column=1, padx=10, pady=10)



        def terminarPartida():
            self.terminarJuego()
            try:
                juego.destroy()
            except:
                pass

            final = Tk()
            final.title("Puntaje Final")
            final.iconbitmap("iconos/ColB.ico")
            frameF = Frame(final)
            frameF.pack()

            frameF1 = Frame(frameF)
            frameF1.grid(row=0, column=0)

            frameF2 = Frame(frameF)
            frameF2.grid(row=0, column=1)

            nombre = StringVar()
            nombre.set(self.__nombre)
            label_0 = Label(frameF2, textvariable=nombre)
            label_0.grid(row=0, column=0)

            label_1 = Label(frameF2, text="Partida terminada\nTu puntaje fue:")
            label_1.grid(row=1, column=0)

            pun = StringVar()
            pun.set(str(self.__puntaje))
            label_3 = Label(frameF2, textvariable=pun)
            label_3.grid(row=2, column=0)

            textohis = StringVar()
            textohis.set(self.leerHistoricos())
            label_2 = Label(frameF1, textvariable=textohis)
            label_2.grid(row=1, column=0)

            label_4 = Label(frameF1, text="Marcador")
            label_4.grid(row=0, column=0)

            def volverInicio():
                final.destroy()
                self.__init__()
                self.lanzarJuego()


            botonF = Button(frameF2, text="Inicio", command=lambda: volverInicio())
            botonF.grid(row=3, column=0, padx=10, pady=10)

            final.mainloop()


        botonSalir = Button(miFrame8, text="Abandonar \nPartida", command=lambda: terminarPartida())
        botonSalir.grid(row=0, column=0, padx=10, pady=10)

        def respuestaPregunta():
            juego.destroy()
            if self.__bandera == 1:
                self.validarResultados(respuesta, opcion1)
            elif self.__bandera == 2:
                self.validarResultados(respuesta, opcion2)
            elif self.__bandera == 3:
                self.validarResultados(respuesta, opcion3)
            elif self.__bandera == 4:
                self.validarResultados(respuesta, opcion4)

            if self.__categoria == 5:
                terminarPartida()

        botonConfirmar = Button(miFrame8, text="Confirmar \nRespuesta", command=lambda: respuestaPregunta())
        botonConfirmar.grid(row=0, column=1, padx=10, pady=10)

        juego.mainloop()


juego1 = PlayColombia()
juego1.lanzarJuego()
