from tkinter import *

root =Tk()

canvas = Canvas(root, width = 400, height = 400,)

canvas.pack()

img = PhotoImage(file = "fodboldja.png")

canvas.create_image(20,20, anchor = NW, image=img)

mainloop()