import tkinter as tk
from tkinter import *

window = Tk()
window.title("Diffrencial og Intergral")
window.geometry("500x250")


main_frame = tk.Frame(window)
Titel = Label(window, text = "Insert titel", font=("Arial Bold", 25), padx = 250, pady = 50)
Titel.pack()

def clickone():
    Titel.configure(text = "Hello")

def clicktwo():
    Titel.configure(text = "There")

Differencial = tk.Button(window, text = "Differencialregning", command = clickone, height = 2, width = 15, padx = 50)
Differencial.pack()

Intergral = tk.Button(window, text = "Intergralregning", command = clicktwo, height = 2, width = 15, padx = 50)
Intergral.pack()

window.mainloop()