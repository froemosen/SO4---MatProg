#MESAM = 'Mathematical Equation Solver And More' aka vores script med matematiske funktioner. 
import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import sin, cos, tan, pi
import main
def decode(ligningRaw):
    try:
        ligningString = "" #Output som decodes af sympy til sidst
        prevTegn = "" #Tidligere tegn brugt i for loop
        nextTegn = "" #Næste tegn i for loop
        nextNextTegn = "" #Tegnet efter næste tegn i for loop
        noInList = 0 #Bruges til at kunne finde tegn som kommer efter nuværende
        cooldown = 0 #Bruges til cos, sin, tan og pi
        ligningList = list(ligningRaw) #Liste med et tegn per plads, dannet ud fra inputtet

        for tegn in ligningList:
            try:
                nextTegn = ligningList[noInList+1]   
            except: #Hvis der ikke er flere tegn tilbage efterfølgende
                pass 
            try:
                nextNextTegn = ligningList[noInList+2]
            except: #Hvis der ikke er to tegn tilbage
                pass
            
            if cooldown == 0:           
                if tegn.lower()+nextTegn.lower()+nextNextTegn.lower() == "sin": #Tjek om sinus bruges
                    tegn = "sin"
                    if prevTegn == "*" or prevTegn == "" or prevTegn == "*" or prevTegn == "**" or prevTegn == "(" or prevTegn == "+" or prevTegn == "-" or prevTegn =="/":
                        prevTegn = ""
                    else:
                        prevTegn = "*"
                    cooldown = 2

                elif tegn.lower()+nextTegn.lower()+nextNextTegn.lower() == "cos": #Tjek om cosinus bruges
                    tegn = "cos"
                    if prevTegn == "*" or prevTegn == "" or prevTegn == "*" or prevTegn == "**" or prevTegn == "(" or prevTegn == "+" or prevTegn == "-" or prevTegn =="/":
                        prevTegn = ""
                    else:
                        prevTegn = "*"
                    cooldown = 2
                
                elif tegn.lower()+nextTegn.lower()+nextNextTegn.lower() == "tan": #Tjek om tangens bruges
                    tegn = "tan"
                    if prevTegn == "*" or prevTegn == "" or prevTegn == "*" or prevTegn == "**" or prevTegn == "(" or prevTegn == "+" or prevTegn == "-" or prevTegn =="/":
                        prevTegn = ""
                    else:
                        prevTegn = "*"

                    cooldown = 2

                elif tegn.lower()+nextTegn.lower() == "pi": #Tjek om pi bruges
                    tegn = "pi"
                    if prevTegn == "*" or prevTegn == "" or prevTegn == "*" or prevTegn == "**" or prevTegn == "(" or prevTegn == "+" or prevTegn == "-" or prevTegn =="/":
                        prevTegn = ""
                    else:
                        prevTegn = "*"
                    cooldown = 1

                elif tegn == "^": #Tjek om noget opløftes med "^"
                    tegn = "**"
                    prevTegn = ""
                
                #Indsætter gangetegn hvis man skriver f.eks. 2x-3x -> 2*x-3*x
                elif prevTegn != "*" and prevTegn != "**" and prevTegn != "" and prevTegn != "(" and prevTegn != "+" and prevTegn != "-" and prevTegn != "/" and tegn.isalpha():
                    prevTegn = "*"
                    tegn = "x"
                
                elif tegn.isalpha() and prevTegn == "" or prevTegn == "(": #Lader være med at indsætte gangetegn i nogle tilfælde
                    tegn = "x"
                    prevTegn = ""

                else: #Tegnet tages med, men intet nyt tilføjes
                    prevTegn = ""
                
                ligningString += prevTegn
                ligningString += tegn
                prevTegn = tegn
            else:
                cooldown -= 1
                

            noInList += 1

        print("Ligning før omdannelse: "+ligningString)
        ligningReady = sympy.sympify(ligningString)
        print("Ligningen i python-sprog: ", ligningReady)
        return ligningReady    

    except:
        pass
        print("Kunne ikke fortolke ligningen. Prøv igen. (Hint: Brug muligvis standard python-sprog til at skrive ligningen ind)")   


def printGraf(ligningReady, xakselen):
    xAkseLen = abs(int(xakselen))
    perX = 100/xAkseLen+5
    newx = -xAkseLen
    xValues = []
    yValues = []
    #plt.grid() #VI VED IKKE OM VI STADIG BRUGER PLT
    for value in range(int(xAkseLen*perX*2)):
        try:
            oldx = newx
            oldfx = ligningReady.subs(dict(x=oldx))
            print("oldfx:",oldfx)
            newx = oldx+1/perX
            newfx = ligningReady.subs(dict(x=newx))
            print("newfx:",newfx)

            if abs(newfx) < abs((oldfx+50)*1000) and abs(oldfx) < abs((newfx+50)*1000): #Er med til at gøre grafen mere brugervenlig, da den sorterer helt vildt høje/lave y-værdier fra
                xValues.append(float(newx))
                yValues.append(float(newfx))
            else:
                pass
        except:
            print("Lille fejl - y-værdi blev nok for høj, men fortsætter")

    return (xValues, yValues)

    #lavTangent(xAkseLen, ligningReady)
        
         
def lavTangent(xakselen, ligningReady, xTangent): #MANGLER AT BLIVE LAVET OM TIL AT RETURNERE VÆRDIER
    xAkseLen = abs(int(xakselen))
    xTangent = float(xTangent)
    deltax = abs(xTangent)*5+1 #Start deltax

    x1 = xTangent-deltax
    x2 = xTangent+deltax
    y1 = ligningReady.subs(dict(x=x1))
    y2 = ligningReady.subs(dict(x=x2))


    stigning = (y2-y1)/(x2-x1)
    prevStigning = stigning*1.1+10

    try:
        for i in range(200):
            deltax /= 2

            x1 = xTangent-deltax/2
            x2 = xTangent+deltax
            y1 = ligningReady.subs(dict(x=x1))
            y2 = ligningReady.subs(dict(x=x2))

            stigning = (y2-y1)/(x2-x1)
            b=(y1)-(stigning)*(x1)

            if abs(abs(prevStigning)-abs(stigning)) < 10**(-7):
                bundTangentX = xAkseLen
                topTangentX = -xAkseLen
                bundTangentY = stigning*bundTangentX+b
                topTangentY = stigning*topTangentX+b
                print("\nHældningstal i punkt:  a =", stigning)
                print("Tangentensligning:     t(x) = " + str(stigning)+"x + "+str(b)) #Nyt symbol i stedet for x
                return ([bundTangentX, topTangentX], [bundTangentY, topTangentY], stigning, b)
                break

            prevStigning = stigning
            prevB = b
    
    except:
        print("WRONG, but still")
        print("\nHældningstal i punkt:  a =", prevStigning)
        print("Tangentensligning:     t(x) = " + str(prevStigning)+"x"+str(prevB)) #Nyt symbol i stedet for x?


def integral(ligningReady, minX, maxX):
    n = maxX-minX
    
    steps = 1
    
    xValues = []
    yValues = []

    currentX = maxX
    currentA = 0
    prevA = 7

    for i in range(13):
        deltax = n/steps

        for stepNo in range(steps): #Find værdier for x og y
            if stepNo == 0:
                xValues.append(maxX)
                yValues.append(ligningReady.subs(dict(x=maxX)))
            else:
                xValues.append(maxX-(deltax*stepNo))
                yValues.append(ligningReady.subs(dict(x=maxX-deltax*stepNo)))

        for value in yValues: #Udregn currentA
            individuelAreal = deltax*value
            currentA += abs(individuelAreal)

        print(currentA)
        if abs(currentA-prevA) < 10**(-3): #Tjek om areal er tilpas tæt på egentlige areal
            break

        if i == 12: #Lader være med at cleare x- og y-værdierne hvis det er sidste gang funktionen køres. 
            pass

        else:
            xValues.clear()
            yValues.clear()
            currentA = 0

            steps *= 2

    
    return (xValues, yValues, currentA, n)

    #Liste med x'er
    #Lister med y'er (Y_2)
    #Y_1 = 0
    #Gab = deltax/opdeling
    #Areal
    #https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.fill_between.html#matplotlib.pyplot.fill_between


def differencialx1000(ligningReady, xakselen):
    xAkseLen = int(abs(xakselen))
    n = xAkseLen*2

    minX = -xAkseLen
    maxX = xAkseLen

    xValues = []
    yValues = []
    
    for run in range(int(((n+100)/(n/2))*n)): #Udregningen opdeler 1x i et vidst antal felter. Det bliver så ganget med det totale antal felter (n)
        DELTAX = (run+1)/((n+100)/(n/2)) #Deltax i forhold til trinnet som køres
        print(DELTAX) #Ender med at være xAkseLen*2
        xTangent = minX+DELTAX
        
        deltax = abs(xTangent)*5+1 #Start deltax

        x1 = xTangent-deltax/2 #Divideres med to, da nogle ligninger får samme hældningstal to gange i streg
        x2 = xTangent+deltax
        y1 = ligningReady.subs(dict(x=x1))
        y2 = ligningReady.subs(dict(x=x2))


        stigning = (y2-y1)/(x2-x1)
        prevStigning = stigning*1.1+10

        for i in range(200): #Hældningen i punkt som er fundet (Samme son lavTangent())
            deltax /= 2
 
            x1 = xTangent-deltax/2
            x2 = xTangent+deltax
            y1 = ligningReady.subs(dict(x=x1))
            y2 = ligningReady.subs(dict(x=x2))

            stigning = (y2-y1)/(x2-x1)

            if abs(abs(prevStigning)-abs(stigning)) < 10**(-4):
                xValues.append(xTangent)
                yValues.append(stigning)
                break
            
            prevStigning = stigning
    print(xValues, yValues)
    return(xValues, yValues)