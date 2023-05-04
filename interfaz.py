import tkinter

class Interface():
    def __init__(self):

        #Implementando TKINTER
            self.window = tkinter.Tk()
            self.window.geometry("400x300")
            self.window.title("Teoria de errores en funciones")
            self.window.config(background="#333333")

            w = 915
            h = 900
            
            #Posiciona la ventana en el medio de la pantalla
            xPos = self.window.winfo_screenwidth()/2-w/2
            yPos = self.window.winfo_screenheight()/2-h/2
            self.window.geometry('%dx%d+%d+%d' % (w, h, xPos, yPos))

            title1 = tkinter.Label(self.window,
                               text="Ingrese funcion: ",
                               font='Helvetica 10 bold',
                               background="#333333",
                               fg="#519ABA")
            
            self.funcion = tkinter.Entry(self.window,
                                      background="#606060",
                                      fg="#FFFFFF",
                                      text="Funcion",
                                      font="Helvetica 10 bold",
                                      highlightthickness=1,
                                      width= 50,
                                      )
            
            self.x = tkinter.Entry(self.window,
                                      background="#606060",
                                      fg="#FFFFFF",
                                      text="Funcion",
                                      font="Helvetica 10 bold",
                                      highlightthickness=1,
                                      width= 10,
                                      )
            
            self.cotax = tkinter.Entry(self.window,
                                      background="#606060",
                                      fg="#FFFFFF",
                                      text="Funcion",
                                      font="Helvetica 10 bold",
                                      highlightthickness=1,
                                      width= 10,
                                      )
            
            self.y = tkinter.Entry(self.window,
                                      background="#606060",
                                      fg="#FFFFFF",
                                      text="Funcion",
                                      font="Helvetica 10 bold",
                                      highlightthickness=1,
                                      width= 10,
                                      )
            
            self.cotay = tkinter.Entry(self.window,
                                      background="#606060",
                                      fg="#FFFFFF",
                                      text="Funcion",
                                      font="Helvetica 10 bold",
                                      highlightthickness=1,
                                      width= 10,
                                      )
            
            self.z = tkinter.Entry(self.window,
                                      background="#606060",
                                      fg="#FFFFFF",
                                      text="Funcion",
                                      font="Helvetica 10 bold",
                                      highlightthickness=1,
                                      width= 10,
                                      )
            self.cotaz = tkinter.Entry(self.window,
                                      background="#606060",
                                      fg="#FFFFFF",
                                      text="Funcion",
                                      font="Helvetica 10 bold",
                                      highlightthickness=1,
                                      width= 10,
                                      )
            
            titlex = tkinter.Label(self.window,
                               text="Ingrese valor de X y cota de error:",
                               font='Helvetica 10 bold',
                               background="#333333",
                               fg="#519ABA")
            
            titley = tkinter.Label(self.window,
                               text="Ingrese valor de Y y cota de error:",
                               font='Helvetica 10 bold',
                               background="#333333",
                               fg="#519ABA")
            
            titlez = tkinter.Label(self.window,
                               text="Ingrese valor de Z y cota de error:",
                               font='Helvetica 10 bold',
                               background="#333333",
                               fg="#519ABA")
            
            btnCalcErrorX = tkinter.Button(self.window,
                                 text="Calcular error absoluto de X",
                                 width= 25,
                                 height=3,
                                 background="#519ABA",
                                 border=0,
                                 fg="#FFFFFF",
                                 font="Helvetica 10 bold",
                                 activebackground='#1E1E1E',
                                 activeforeground='#519ABA',
                                 relief='solid',
                                 )
            
            btnCalcErrorY = tkinter.Button(self.window,
                                 text="Calcular error absoluto de Y",
                                 width= 25,
                                 height=3,
                                 background="#519ABA",
                                 border=0,
                                 fg="#FFFFFF",
                                 font="Helvetica 10 bold",
                                 activebackground='#1E1E1E',
                                 activeforeground='#519ABA',
                                 relief='solid',
                                 )
            
            btnCalcErrorZ = tkinter.Button(self.window,
                                 text="Calcular error absoluto de Z",
                                 width= 25,
                                 height=3,
                                 background="#519ABA",
                                 border=0,
                                 fg="#FFFFFF",
                                 font="Helvetica 10 bold",
                                 activebackground='#1E1E1E',
                                 activeforeground='#519ABA',
                                 relief='solid',
                                 )
            btnCalcErrorFuncion = tkinter.Button(self.window,
                                 text="Calcular error absoluto de funcion",
                                 width= 25,
                                 height=3,
                                 background="#519ABA",
                                 border=0,
                                 fg="#FFFFFF",
                                 font="Helvetica 10 bold",
                                 activebackground='#1E1E1E',
                                 activeforeground='#519ABA',
                                 relief='solid',
                                 )
            
            title1.place(x=20, y=20)
            self.funcion.place(x=20, y=40)
            titlex.place(x=20, y=70)
            self.x.place(x=20, y=90)
            self.cotax.place(x=120, y=90)
            titley.place(x=20, y=110)
            self.y.place(x=20, y=130)
            self.cotay.place(x=120, y=130)
            titlez.place(x=20, y=150)
            self.z.place(x=20, y=170)
            self.cotaz.place(x=120, y=170)
            btnCalcErrorX.place(x=20, y=280)
            btnCalcErrorY.place(x=260, y=280)
            btnCalcErrorZ.place(x=500, y=280)
            btnCalcErrorFuncion.place(x=20,y=420)
            self.window.mainloop()
app = Interface()