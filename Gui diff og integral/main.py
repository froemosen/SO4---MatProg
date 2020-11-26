import tkinter as tk #en ikke-terminal-baseret version af Differencialregning.py
import mesam
import matplotlib #graf plotter funktionaliteten
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk #importere toolbar til graf
from matplotlib.figure import Figure #impotere grafen

#Skelet for siderne.
class page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

#En selve siderne.
class MainMenu(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)
        text = tk.Label(self, text = "Main Menu")
        text.pack(side = "top", fill = "both", expand = True)

        text2 = tk.Label(self, text = "intro til opgaven")
        text2.pack(side = "top", fill = "both", expand = True)

class VisGraf(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self,*args, **kwargs)

class Differencial(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)

        #ligningRaw = str(int())
        #xAkseLen = str(int())
        #xTangent = str(int())
        
         
        
        text = tk.Label(self, text = "Skriv en ligning")
        self.ligningInput = tk.Entry(self)

        text2 = tk.Label(self, text = "Længde på x-akse i begge retninger")
        self.xAkseLenInput = tk.Entry(self)

        text3 = tk.Label(self, text = "Vælg en x-værdi (Punkt hvor du vil finde hældning)")
        self.xTangentInput = tk.Entry(self)

        btn_beregn = tk.Button(self, text = "Tegn og beregn", command = self.get)

        



        text.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.ligningInput.grid(row = 1, column = 0, padx = 5, pady = 5)
        text2.grid(row = 2, column = 0, padx = 5, pady = 5,)
        self.xAkseLenInput.grid(row = 3, column = 0, padx = 5, pady = 5)
        text3.grid(row = 4, column = 0, padx = 5, pady = 5)
        self.xTangentInput.grid(row = 5, column = 0, padx = 5, pady = 5)
        btn_beregn.grid(row = 6, column = 0, padx = 5, pady = 5)        

    def get(self):
            ligningRaw = str(self.ligningInput.get())
            xAkseLen = int(self.xAkseLenInput.get())
            xTangent = float(self.xTangentInput.get())

            self.window(ligningRaw, xAkseLen, xTangent)


    def window(self, ligningRaw, xAkseLen, xTangent):
            ligning = mesam.decode(ligningRaw)
            Xvalues, Yvalues = mesam.printGraf(ligning, xAkseLen)
            xerTilTangent, yerTilTangent = mesam.lavTangent(xAkseLen, ligning, xTangent)
            f = Figure(figsize=(8, 5), dpi=80) #Bestemmer størelsen af grafen sammen med nedenstående linje
            a = f.add_subplot(111)             #Bestemmer størelsen af grafen sammen med ovenstående linje
            a.plot(Xvalues, Yvalues)  #Den data der bliver plottet på grafen
            a.plot(xerTilTangent, yerTilTangent, "-m") #TangentLinje
            a.plot(xTangent, mesam.sympy.sympify(ligning.subs(dict(x=xTangent))), "m*")
            # (Grafen autoscaler)
            #tangent = f.add_subplot(111)
            canvas = FigureCanvasTkAgg(f, self) #Give "FigureCanvasTkAgg" de argumenter den skal bruge, foreksempel størelse)
            canvas.draw() #Tegner grafen ud fra givet argumenter
            canvas.get_tk_widget().grid(row = 0, column = 1, rowspan = 100) #Smider det ind i vinduet

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False) #Tager imod de relevante argumenter og info
            toolbar.grid(row = 101, column = 1)
            toolbar.update() #tjekker om den bliver brugt

class Intergral(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)
        text = tk.Label(self, text = "General Konobi!!!")
        text.pack(side = "top", fill = "both", expand = True)


#Laver variabler til knapper.
class MainFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        MainMenuWindow = MainMenu(self)
        VisGrafWindow = VisGraf(self)
        DifferencialWindow = Differencial(self)
        IntergralWindow = Intergral(self)
 
        #Laver vi kasser til selve knapperne.
        ButtonFrame = tk.Frame(self,)
        Box = tk.Frame(self,)
        ButtonFrame.pack(side = "left", fill = "x", expand= False)
        Box.pack(side = "left", fill = "both", expand= True)

        #Placering for kasserne
        MainMenuWindow.place(in_= Box, x = 0, y = 0, relwidth = 1, relheight = 1)
        VisGrafWindow.place(in_= Box, x = 0, y = 0, relwidth = 1, relheight = 1)
        DifferencialWindow.place(in_= Box, x = 0, y = 0, relwidth = 1, relheight = 1)
        IntergralWindow.place(in_= Box, x = 0, y = 0, relwidth = 1, relheight = 1)

        #Selve knapperne bliver lavet
        MainMenuButton = tk.Button(ButtonFrame, text = "Main Menu", command = MainMenuWindow.lift)
        VisGrafButton = tk.Button(ButtonFrame, text = "Vis Graf", command = VisGrafWindow.lift)
        DifferencialButton = tk.Button(ButtonFrame, text = "Differencial Regning", command = DifferencialWindow.lift)
        IntergralButton = tk.Button(ButtonFrame, text = "Intergral Regning",  command = IntergralWindow.lift)


        MainMenuButton.grid(row = 0, column = 0, padx = 5, pady = 5,)
        VisGrafButton.grid(row = 1, column = 0, padx = 5, pady = 5)
        DifferencialButton.grid(row = 2, column = 0, padx = 5, pady = 5)
        IntergralButton.grid(row = 3, column = 0, padx = 5, pady = 5)
        

        #Hvilken side programmet skal starte i
        MainMenuWindow.show()

#Får lavet GUIen til koden       
if __name__ == "__main__":
    base = tk.Tk()
    base.title("SO4 opgave")
    main = MainFrame(base)
    main.pack(side = "top", fill = "both", expand = True)
    base.wm_geometry("1000x500") #Vi skal definer en størrelse fordi siden ville collapse ind på kasserne til knapperne 
    base.mainloop()