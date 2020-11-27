import tkinter as tk

root =tk.Tk()

canvas = tk.Canvas(root, width = 1800, height = 800,)


img = tk.PhotoImage(file = "Gui diff og integral/aarhustech.png")

canvas.create_image(900,400, image=img)

canvas.pack()
tk.mainloop()