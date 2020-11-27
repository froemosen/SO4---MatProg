import tkinter as tk
"""
root =tk.Tk()

canvas = tk.Canvas(root, width = 1800, height = 800,)


img = tk.PhotoImage(file = "Gui diff og integral/grafbilledlille.png")

canvas.create_image(1000,400, image=img)

canvas.pack()

tk.mainloop()
"""
root = tk.Tk()
frame = tk.Frame(root)
image = tk.PhotoImage(file='Gui diff og integral/aarhustechSmol.png')
button = tk.Button(frame, image=image)
button.pack()
frame.pack()
root.mainloop()