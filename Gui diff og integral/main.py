import tkinter as tk #en ikke-terminal-baseret version af Differencialregning.py
import matplotlib #graf plotter funktionaliteten
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk #importere toolbar til graf
from matplotlib.figure import Figure #impotere grafen

import meth 
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
        text = tk.Label(self, text = "Main Menu", bg = 'blue')
        text.pack(side = "top", fill = "both", expand = True)

        text2 = tk.Label(self, text = "intro til opgaven", bg ='red')
        text2.pack(side = "top", fill = "both", expand = True)

class Differencial(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)
        text = tk.Label(self, text = "Skriv en ligning", bg ='blue')
        entry = tk.Entry(self)

        text2 = tk.Label(self, text = "Vælg en x-værdi")
        entry2 = tk.Entry(self)

        btn_beregn = tk.Button(self, text = "Tegn og beregn")

        text.pack(side = "top", fill = "both", expand = True)
        entry.pack(side = "top", fill = "none", expand = True)
        text2.pack(side = "top", fill = "both", expand = True)
        entry2.pack(side = "top", fill = "none", expand = True)
        btn_beregn.pack(side = "top", fill = "none", expand = True)


class Intergral(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)
        text = tk.Label(self, text = "General Konobi!!!")
        text.pack(side = "top", fill = "both", expand = True)


class Graf(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)

        f = Figure(figsize=(4, 4), dpi=80) #Bestemmer størelsen af grafen sammen med nedenstående linje
        a = f.add_subplot(111)             #Bestemmer størelsen af grafen sammen med ovenstående linje
        a.plot([1, 2, 3, 4, 5, 6, 7, 8, 10, 12], [5, 6, 1, 3, 8, 9, 3, 5, 10, 12])  #Den data der bliver plottet på grafen
        # (Grafen autoscaler)

        canvas = FigureCanvasTkAgg(f, self) #Give "FigureCanvasTkAgg" de argumenter den skal bruge, freksempel størelse)
        canvas.draw() #Tegner grafen ud fra givet argumenter
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True) #Smider det ind i vinduet

        toolbar = NavigationToolbar2Tk(canvas, self) #Tager imod de relevante argumenter og info
        toolbar.update() #tjekker om den bliver brugt
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True) #Smider det ind i vinduet


#Laver variabler til knapper.
class MainFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        MainMenuWindow = MainMenu(self)
        DifferencialWindow = Differencial(self)
        IntergralWindow = Intergral(self)
        GrafWindow = Graf(self)

        #Laver vi kasser til selve knapperne.
        ButtonFrame = tk.Frame(self, bg = 'green')
        Box = tk.Frame(self,)
        ButtonFrame.pack(side = "left", fill = "y", expand= False,)
        Box.pack(side = "left", fill = "both", expand= True)

        #Placering for kasserne
        MainMenuWindow.place(in_= Box, x = 0, y = 0, relwidth = 1, relheight = 1)
        DifferencialWindow.place(in_= Box, x = 0, y = 0, relwidth = 1, relheight = 1)
        IntergralWindow.place(in_= Box, x = 0, y = 0, relwidth = 1, relheight = 1)
        GrafWindow.place(in_= Box, x = 0, y = 0, relwidth = 1, relheight = 1)

        #Selve knapperne bliver lavet
        MainMenuButton = tk.Button(ButtonFrame, text = "Main Menu", command = MainMenuWindow.lift)
        DifferencialButton = tk.Button(ButtonFrame, text = "Differencial Regning", command = DifferencialWindow.lift) 
        IntergralButton = tk.Button(ButtonFrame, text = "Intergral Regning", command = IntergralWindow.lift)
        GrafButton = tk.Button(ButtonFrame, text = "Graf", command = GrafWindow.lift)

        MainMenuButton.grid(row = 0, column = 0, padx = 5, pady = 5)
        DifferencialButton.grid(row = 1, column = 0, padx = 5, pady = 5)
        IntergralButton.grid(row = 2, column = 0, padx = 5, pady = 5)
        GrafButton.grid(row = 3, column = 0, padx = 5, pady = 5)

        #Hvilken side programmet skal starte i
        MainMenuWindow.show()
"""
class PageThree(tk.Frame):  #denne klasse af koden er hentet på: https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
"""
#Får lavet GUIen til koden       
if __name__ == "__main__":
    base = tk.Tk()
    base.title("SO4 opgave")
    main = MainFrame(base)
    main.pack(side = "top", fill = "both", expand = True)
    base.wm_geometry("1000x500") #Vi skal definer en størrelse fordi siden ville collapse ind på kasserne til knapperne 
    base.mainloop() 