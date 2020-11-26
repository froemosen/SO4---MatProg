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
        text.config(font=("Courier", 44), bg = '#bcc8e8')
        text.pack(side = "top", fill ='x')

        text2 = tk.Label(self, text = "intro til GUI'en")
        text2.config(font=("Courier", 20), bg = '#bcc8e8')
        text2.pack(side = "top", fill = "x")

class VisGraf(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self,*args, **kwargs)

class Differencial(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)  
        
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
            xerTilTangent, yerTilTangent, stigning, b = mesam.lavTangent(xAkseLen, ligning, xTangent)
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

            stigningText = tk.Label(self, text = f"Stigning for tangeten = {stigning}")
            ligningTangentText = tk.Label(self, text = f"t(x) = {stigning}*x + ({b})")

            stigningText.grid(row = 7, column = 0, padx = 5, pady = 10)
            ligningTangentText.grid(row = 8, column = 0, padx = 5, pady = 10)


class Intergral(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)
        text = tk.Label(self, text = "General Konobi!!!")
        text.pack(side = "top", fill = "both", expand = True)

class Differencialx1000(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)
        text = tk.Label(self, text = "General Konobi!!!")
        text.pack(side = "top", fill = "both", expand = True)


#Laver variabler til knapper.
class MainFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs, bg = '#bcc8e8')
        MainMenuWindow = MainMenu(self)
        VisGrafWindow = VisGraf(self)
        DifferencialWindow = Differencial(self)
        IntergralWindow = Intergral(self)
        Differencialx1000Window = Differencialx1000(self)
 
        #Laver vi kasser til selve knapperne.
        ButtonFrame = tk.Frame(self, bg = '#bcc8e8', borderwidth = 3, relief = 'raised')
        Box = tk.Frame(self,)
        ButtonFrame.pack(side = "left", fill = "both", expand= False)
        Box.pack(side = "left", fill = "both", expand= True)

        #Placering for kasserne
        MainMenuWindow.place(in_= Box, x = 0, y = 0, relwidth = 1, relheight = 1)
        VisGrafWindow.place(in_= Box, x = 0, y = 0, relwidth = 1, relheight = 1)
        DifferencialWindow.place(in_= Box, x = 0, y = 0, relwidth = 1, relheight = 1)
        IntergralWindow.place(in_= Box, x = 0, y = 0, relwidth = 1, relheight = 1)
        Differencialx1000Window.place(in_ = Box, x = 0, y = 0, relwidth = 1, relheight = 1)



        #Selve knapperne bliver lavet
        MainMenuButton = tk.Button(ButtonFrame, text = "Main Menu", command = MainMenuWindow.lift)
        VisGrafButton = tk.Button(ButtonFrame, text = "Vis Graf", command = VisGrafWindow.lift)
        DifferencialButton = tk.Button(ButtonFrame, text = "Differencial Regning", command = DifferencialWindow.lift)
        IntergralButton = tk.Button(ButtonFrame, text = "Intergral Regning",  command = IntergralWindow.lift)
        Differencialx1000Button = tk.Button(ButtonFrame, text = "1000x Differencial", command = Differencialx1000Window.lift)

        MainMenuButton.grid(row = 0, column = 0, padx = 5, pady = 20)
        VisGrafButton.grid(row = 1, column = 0, padx = 5, pady = 20)
        DifferencialButton.grid(row = 2, column = 0, padx = 5, pady = 20)
        IntergralButton.grid(row = 3, column = 0, padx = 5, pady = 20)
        Differencialx1000Button.grid(row = 4, column = 0, padx = 5, pady = 20)
        

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