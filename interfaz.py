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
                               text="Ingrese funcion",
                               font='Helvetica 10 bold',
                               background="#333333",
                               fg="#519ABA")
            
            self.calFirst = tkinter.Entry(self.window,
                                      background="#606060",
                                      fg="#FFFFFF",
                                      font="Helvetica 10 bold",
                                      highlightthickness=1,
                                      width= 25,
                                      )
            
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
            
            title1.place(x=20, y=20)
            self.calFirst.place(x=20, y=40)
            btnCalcErrorX.place(x=20, y=150)
            btnCalcErrorY.place(x=260, y=150)
            btnCalcErrorZ.place(x=500, y=150)
            self.window.mainloop()
app = Interface()