import tkinter as tk

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

class Differencial(page):
    def __init__(self, *args, **kwargs):
        page.__init__(self, *args, **kwargs)
        text = tk.Label(self, text = "Hello There")
        text.pack(side = "top", fill = "both", expand = True)

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
        DifferencialWindow = Differencial(self)
        IntergralWindow = Intergral(self)

        #Laver vi kasser til selve knapperne.
        ButtonFrame = tk.Frame(self)
        Box = tk.Frame(self)
        ButtonFrame.pack(side = "top", fill = "x", expand= False)
        Box.pack(side = "top", fill = "both", expand= True)

        #Placering for kasserne
        MainMenuWindow.place(in_= Box, x = 0, y = 0, relwidth = 1, relheight = 1)
        DifferencialWindow.place(in_= Box, x = 0, y = 0, relwidth = 1, relheight = 1)
        IntergralWindow.place(in_= Box, x = 0, y = 0, relwidth = 1, relheight = 1)

        #Selve knapperne bliver lavet
        MainMenuButton = tk.Button(ButtonFrame, text = "Main Menu", command = MainMenuWindow.lift)
        DifferencialButton = tk.Button(ButtonFrame, text = "Differencial Regning", command = DifferencialWindow.lift) 
        IntergralButton = tk.Button(ButtonFrame, text = "Intergral Regning", command = IntergralWindow.lift)

        MainMenuButton.pack(side = "left")
        DifferencialButton.pack(side = "left")
        IntergralButton.pack(side = "left")

        #Hvilken side programmet skal starte i
        MainMenuWindow.show()

#Får lavet GUIen til koden       
if __name__ == "__main__":
    base = tk.Tk()
    main = MainFrame(base)
    main.pack(side = "top", fill = "both", expand = True)
    """base.wm_geometry("500x500")""" #
    base.mainloop() 