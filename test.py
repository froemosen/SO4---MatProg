import tkinter as tk

#--main vindue---
main_window = tk.Tk()
main_window.title("hAALLLOO")
main_window.geometry('400x400')


#----frame1----
frame1=tk.Frame(main_window)
tekst = tk.Label(frame1, text="halloe" )
tekst.grid(row=0)


frame1.grid()


#---frame2---
frame2=tk.Frame(main_window)
tekst2 = tk.Label(frame2, text="halloe" )
tekst2.grid()

frame2.grid()




main_window.mainloop()