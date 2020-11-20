import tkinter as tk
from tkinter import *

window = Tk()
window.title("Diffrencial og Intergral")
window.geometry("500x250")

main_frame = tk.Frame(window)

Differencial = tk.Button(window, text = "Differencialregning")
Differencial.grid(column = 0, row = 0)
Differencial.pack()

Intergral = tk.Button(window, text = "Intergralregning")
Intergral.pack()

window.mainloop()

