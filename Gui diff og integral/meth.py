import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import sin, cos, tan, pi

def decode(ligningRaw):
    try:
        ligningString = ""
        prevTegn = ""
        nextTegn = ""
        nextNextTegn = ""
        noInList = 0
        cooldown = 0
        ligningList = list(ligningRaw)

        for tegn in ligningList:
            try:
                nextTegn = ligningList[noInList+1]
                nextNextTegn = ligningList[noInList+2]
            except:
                pass
            
            if cooldown == 0:           
                if tegn.lower()+nextTegn.lower()+nextNextTegn.lower() == "sin":
                    tegn = "sin"
                    cooldown = 2

                elif tegn.lower()+nextTegn.lower()+nextNextTegn.lower() == "cos":
                    tegn = "cos"
                    cooldown = 2
                
                elif tegn.lower()+nextTegn.lower()+nextNextTegn.lower() == "tan":
                    tegn = "tan"
                    cooldown = 2

                elif tegn.lower()+nextTegn.lower() == "pi":
                    tegn = "pi"
                    cooldown = 1

                elif tegn == "^":
                    tegn = "**"
                    prevTegn = ""
                
                elif prevTegn != "*" and prevTegn != "**" and prevTegn != "" and prevTegn != "(" and prevTegn != "+" and prevTegn != "-" and prevTegn != "/" and tegn.isalpha():
                    prevTegn = "*"
                    tegn = "x"
                
                elif tegn.isalpha() and prevTegn == "" or prevTegn == "(":
                    tegn = "x"
                    prevTegn = ""

                else:
                    prevTegn = ""
                
                ligningString += prevTegn
                ligningString += tegn
                prevTegn = tegn
            else:
                cooldown -= 1
                

            noInList += 1

        #print("Ligning før omdannelse: "+ligningString)
        ligningReady = sympy.sympify(ligningString)
        #print("Ligningen i python-sprog: ", ligningReady)
        return ligningReady
        

    except:
        return 0
        pass #FJERN SENERE
        #print("Kunne ikke fortolke ligningen. Prøv igen. (Hint: Brug muligvis standard python-sprog til at skrive ligningen ind)")
    

def printGraf(ligningReady, xAkselen):
    xAkseLen = abs(int(xAkseLen))
    newx = -xAkseLen
    #plt.grid() #VI VED IKKE OM VI STADIG BRUGER PLT
    for value in range(xAkseLen*20*2):
        try:
            oldx = newx
            oldfx = ligningReady.subs(dict(x=oldx))
            print("oldfx:",oldfx)
            newx = oldx+1/20
            newfx = ligningReady.subs(dict(x=newx))
            print("newfx:",newfx)

            if abs(newfx) < abs((oldfx+50)*1000) and abs(oldfx) < abs((newfx+50)*1000): #Er med til at gøre grafen mere brugervenlig, da den sorterer helt vildt høje/lave y-værdier fra
                #plt.plot([oldx, newx], [oldfx, newfx])
                #Plot smthn her - idk how
                pass
            else:
                pass
        except:
            print("Lille fejl - y-værdi blev nok for høj, men fortsætter")

    #lavTangent(xAkseLen, ligningReady)
        
        
    
def lavTangent(xAkseLen, ligningReady, xTangent):
    xTangent = float(xTangent)
    deltax = abs(xTangent)*5+1 #Start deltax

    timeToPause = 0.7

    x1 = xTangent-deltax
    x2 = x1+deltax
    y1 = ligningReady.subs(dict(x=x1))
    y2 = ligningReady.subs(dict(x=x2))


    stigning = (y2-y1)/(x2-x1)
    prevStigning = stigning+1

    try:
        for execution in range(3000):
            deltax /= 2

            x1 = xTangent-deltax
            x2 = xTangent+deltax
            y1 = ligningReady.subs(dict(x=x1))
            y2 = ligningReady.subs(dict(x=x2))

            stigning = (y2-y1)/(x2-x1)
            b=(y1)-(stigning)*(x1)

            if abs(abs(prevStigning)-abs(stigning)) < 10**(-7):
                print("\nHældningstal i punkt:  a =", stigning)
                print("Tangentensligning:     t(x) = " + str(stigning)+"x + "+str(b)) #Nyt symbol i stedet for x?
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

            #tangent = plt.plot([bundTangentX, topTangentX], [bundTangentY, topTangentY])

            timeToPause /= 2
            prevStigning = stigning
            prevB = b

            #plt.pause(timeToPause)
    except:
        print("\nHældningstal i punkt:  a =", prevStigning)
        print("Tangentensligning:     t(x) = " + str(prevStigning)+"x"+str(prevB)) #Nyt symbol i stedet for x?

