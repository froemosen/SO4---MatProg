"""
import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
"""

import mesam
import sympy
import numpy
import matplotlib.pyplot as plt
from sympy import sin

ligning = sympy.sympify("sin(x)*x")
x0 = 10
x1 = 14

xValues, yValues, areal, deltax = mesam.integral(ligning, x0, x1)

#print("xValues:", xValues)
#print("yValues:", yValues)
print("areal:", areal)
print("deltax:", deltax)

#plt.plot([x0, x0], [0, ligning.subs(dict(x=x0))], "-m")

print(len(xValues))
print(len(yValues))

for linje in range(32):
    print(int((len(yValues)-1)*(linje+1)/32))
    xLinje = xValues[int((len(xValues)-1)*(linje+1)/32)]
    yLinje = yValues[int((len(yValues)-1)*(linje+1)/32)]
    print(xLinje, yLinje)
    plt.plot([xLinje, xLinje], [0, yLinje], "-m")
  
#plt.plot([x1, x1], [0, ligning.subs(dict(x=x1))], "-m")

"""
xValuesFill = numpy.linspace(x0, x1)
yValuesFill = numpy.array(yValues, dtype=float)
plt.fill_between(xValuesFill, yValuesFill, 0, color="blue")
"""

#plt.fill(xValues, yValues, zorder=10)

plt.show()
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
###############################################################################
# First, the most basic fill plot a user can make with matplotlib:

fig, ax = plt.subplots()

ax.fill(x, y, zorder=10)
ax.grid(True, zorder=5)

x = np.linspace(0, 2 * np.pi, 500)
y1 = np.sin(x)
y2 = np.sin(3 * x)

###############################################################################
# Next, a few more optional features:
#
# * Multiple curves with a single command.
# * Setting the fill color.
# * Setting the opacity (alpha value).

fig, ax = plt.subplots()
ax.fill(x, y1, 'b', x, y2, 'r', alpha=0.3)
plt.show()
"""