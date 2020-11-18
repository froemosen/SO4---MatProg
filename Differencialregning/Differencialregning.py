import numpy as np
import matplotlib.pyplot as plt

xAkseLen = int(input("Længde på x-aksen: "))
plt.grid()
newx = -xAkseLen
for value in range(xAkseLen*100*2):
    oldx = newx
    oldfx = oldx**2+10*oldx+10
    newx = oldx+0.01
    newfx = newx**2+10*newx+10
    plt.plot([oldx, newx], [oldfx, newfx])
    



xTangent = float(input("Punkt på funktionen hvor du vil finde hældning: "))
deltax = xTangent/10 #Start deltax
prevDeltax = xTangent+1
for execution in range(1000):
    deltax /= 2

    y1 = xTangent**2+10*xTangent+10
    y2 = (xTangent+deltax)**2+10*(xTangent+deltax)+10
    x1 = xTangent
    x2 = xTangent+deltax

    try:
        stigning = (y2-y1)/(x2-x1)
    except:
        stigning = (y1-y2)/(x1-x2)

    if prevDeltax-deltax > 10**(-8):
        print("a =", stigning)
        break

    prevDeltax = deltax


plt.show()
print("\nDin funktion bliver nu indtegnet i et koordinatsystem\n")
"""
plt.axis([0, 10, 0, 1])

for i in range(100):
    y = np.random.random()
    x = np.random.random()
    plt.scatter(x, y)
    plt.pause(0.5)

plt.show()
"""