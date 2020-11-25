import tkinter as tk

root =tk.Tk()

canvas = tk.Canvas(root, width = 400, height = 400,)


img = tk.PhotoImage(file = "Gui diff og integral/fodboldja.png")

canvas.create_image(100,100, image=img)

canvas.pack()
tk.mainloop()