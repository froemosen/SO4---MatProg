import tkinter as tk
from tkinter import *
from tkinter.ttk import *

window = Tk()
# window.title("Diffrencial og Intergral")
window.geometry("500x250")

def OpenDifferencialWindow():
    DifferencialWindow = Toplevel(window)
    DifferencialWindow.title("Differencial Regning")
    DifferencialWindow.geometry("500x250")
    Label(DifferencialWindow, text = "Something")

def OpenIntergralWindow():
    IntergralWindow = Toplevel(window)
    IntergralWindow.title("Intergral Regning")
    IntergralWindow.geometry("500x250")
    Label(IntergralWindow, text = "Something")


main_frame = tk.Frame(window)
Titel = Label(window, text = "Insert titel")
Titel.pack()

Differencial = tk.Button(window, text = "Differencialregning", command = OpenDifferencialWindow, height = 2, width = 15, padx = 50)
Differencial.pack()

Intergral = tk.Button(window, text = "Intergralregning", command = OpenIntergralWindow, height = 2, width = 15, padx = 50)
Intergral.pack()

Indtastning = tk.Entry(window,width = 50)
Indtastning.pack()

window.mainloop()