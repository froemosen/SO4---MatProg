import tkinter as tk

root =tk.Tk()

canvas = tk.Canvas(root, width = 1204, height = 1280,)

img = tk.PhotoImage(file = "Gui diff og integral/fodboldja.png")

canvas.create_image(602,640, image=img)

canvas.pack()
tk.mainloop()