from tkinter import *

root =Tk()

canvas = Canvas(root, width = 100, height = 100,)

canvas.pack()

img = PhotoImage(file = "C\Users\Lenovo\Documents\GitHub\SO4---MatProg\Gui diff og integral\fodboldja.png")

canvas.create_image(20,20, anchor = NW, image=img)

mainloop()