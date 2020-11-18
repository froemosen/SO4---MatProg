import numpy as np
import matplotlib.pyplot as plt
import sympy

print("\n_______NU STARTER PROGRAM TIL DIFFENRENCIALREGNING_______\n")

print("Guide til ligning:\n    Indtast ligning på en de måder som ses i eksempler herunder:    (Max 1 variabel!)\n        - Python-sprog: a*x**2+b\n        - Normal-sprog: ax^2+b\n        - Blanding: a*x^2+b\n")

def decode():
    ligningString = ""
    prevTegn = ""
    ligningList = list(input("Indtast ligning: "))
    for tegn in ligningList:
        if tegn == "^":
            tegn = "**"
        if tegn.isalpha():
            tegn = "x"
        
        if prevTegn.isdigit() and tegn.isalpha():
            prevTegn = "*"
        else:
            prevTegn = ""
        
        ligningString += prevTegn
        ligningString += tegn
        prevTegn = tegn

    ligningReady = sympy.sympify(ligningString)
    print("Ligningen i python-sprog: ", ligningReady)
    printGraf(ligningReady)

    

def printGraf(ligningReady):
    xAkseLen = int(input("\nLængde på x-aksen i begge retninger: "))
    plt.grid()
    newx = -xAkseLen
    for value in range(xAkseLen*100*2):
        oldx = newx
        oldfx = ligningReady.subs(dict(x=oldx))
        newx = oldx+0.01
        newfx = ligningReady.subs(dict(x=newx))
        plt.plot([oldx, newx], [oldfx, newfx])
    
    lavTangent(xAkseLen, ligningReady)
    
def lavTangent(xAkseLen, ligningReady):
    xTangent = float(input("\nPunkt på funktionen hvor du vil finde hældning: "))
    deltax = xTangent*5+1 #Start deltax
    prevDeltax = deltax+1
    timeToPause = 0.5

    for execution in range(1000):
        deltax /= 2

        y1 = ligningReady.subs(dict(x=xTangent))
        y2 = ligningReady.subs(dict(x=xTangent+deltax))
        x1 = xTangent
        x2 = xTangent+deltax

        try:
            stigning = (y2-y1)/(x2-x1)
            b=(y1)-(stigning)*(x1)
            if prevDeltax-deltax < 10**(-20) and prevDeltax-deltax > 0:
                print("\nHældningstal i punkt:  a =", stigning)
                print("Tangentensligning:     t(x) = " + str(stigning)+"x"+str(b)) #Nyt symbol i stedet for x?
                break

            elif prevDeltax-deltax > -(10**(-20)) and abs(prevDeltax)-abs(deltax) < 0:
                print("\nHældningstal i punkt:  a =", stigning)
                print("Tangentensligning:     t(x) = " + str(stigning)+"x"+str(b)) #Nyt symbol i stedet for x?
                break
        except:
            stigning = (y2-y1)/(x2-x1)
            b=(y1)-(stigning)*(x1)
            if prevDeltax-deltax < 10**(-8) and prevDeltax-deltax > 0:
                print("\nHældningstal i punkt:  a =", stigning)
                print("Tangentensligning:     t(x) = " + str(stigning)+"x"+str(b)) #Nyt symbol i stedet for x?
                break

            elif prevDeltax-deltax > -(10**(-8)) and prevDeltax-deltax < 0:
                print("\nHældningstal i punkt:  a =", stigning)
                print("Tangentensligning:     t(x) = " + str(stigning)+"x"+str(b)) #Nyt symbol i stedet for x?
                break
        finally:
            stigning = (y2-y1)/(x2-x1)
            b=(y1)-(stigning)*(x1)
            if prevDeltax-deltax < 10**(-4) and prevDeltax-deltax > 0:
                print("\nHældningstal i punkt:  a =", stigning)
                print("Tangentensligning:     t(x) = " + str(stigning)+"x"+str(b)) #Nyt symbol i stedet for x?
                break

            elif prevDeltax-deltax > -(10**(-4)) and prevDeltax-deltax < 0:
                print("\nHældningstal i punkt:  a =", stigning)
                print("Tangentensligning:     t(x) = " + str(stigning)+"x"+str(b)) #Nyt symbol i stedet for x?
                break

        try:
            line = tangent.pop(0)
            line.remove()
        except:
            pass

        
        bundTangentX = xAkseLen
        topTangentX = -xAkseLen
        bundTangentY = stigning*xAkseLen+b
        topTangentY = stigning*-(xAkseLen)+b

        

        tangent = plt.plot([bundTangentX, topTangentX], [bundTangentY, topTangentY])
        timeToPause /= 1.5
        prevDeltax = deltax

        plt.pause(timeToPause)
        
if __name__ == '__main__':
    decode()
    plt.show()
"""
plt.axis([0, 10, 0, 1])

for i in range(100):
    y = np.random.random()
    x = np.random.random()
    plt.scatter(x, y)
    plt.pause(0.5)

plt.show()
"""
