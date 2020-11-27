import tkinter as tk

root =tk.Tk()

canvas = tk.Canvas(root, width = 1800, height = 800,)


img = tk.PhotoImage(file = "Gui diff og integral/grafbilledlille.png")

canvas.create_image(1000,400, image=img)

canvas.pack()

tk.mainloop()