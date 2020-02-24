#!/usr/bin/env python3
# -- coding: utf-8 --



# Importation des modules
from tkinter import *
from tkinter.messagebox import *
from random import *
import time




#Variables
taille = 20
pourcentageVivant = 17
etatCell = []   #map avec état cell à l'étape a
etatCell2 = []  #map avec état cell à l'étape a+1
#speed = IntVar()
pause = 0.1



#Fenetre Principale
Fenetre = Tk()
Fenetre.title("Jeu de la Vie by Marius")



#Cases pour les composants de la fenêtre
frameJeu = LabelFrame(Fenetre, text = "Jeu de la Vie")
frameJeu.grid(row = 0, column = 0, sticky = "news")

frameReglages = LabelFrame(Fenetre, text = "Réglages")
frameReglages.grid(row = 1, column = 0, sticky = "news")





#Génération

def generation():

    #mise en place du tableau et remplissage des cell vivantes et mortes

    for i in range(0, taille):
        etatCell.append([])
        etatCell2.append([])

        for j in range(0, taille):
            etatCell[i].append([])      #Double tableaux de coordonnées [x][y] avec True/False pour état cell
            etatCell2[i].append([])

            if randint(0, 100) < pourcentageVivant: #Remplissage du tableau True/False avec le pourcentage donné
                etatCell[i][j] = True
            else:
                etatCell[i][j] = False


#Fenetre

def initialisationFenetre():
    global speed
    #Création de la fenetre avec case vertes si cell vivante et case grise si cell morte

    for i in range(0, taille):
        frameJeu.columnconfigure(i, weight = 1)
        frameJeu.rowconfigure(i, weight = 1)


    for i in range(0, taille):
        for j in range(0, taille):
            if etatCell[i][j] == True:
                Label(frameJeu, text = "   ", relief = GROOVE, borderwidth = 1, bg = "chartreuse").grid(row = i, column = j, sticky = "news")
            else:
                Label(frameJeu, text = "   ", relief = GROOVE, borderwidth = 1, bg = "light grey").grid(row = i, column = j, sticky = "news")


    #Slider de vitesse
    speed = IntVar()
    speed = 100
    scaleVitesse = Scale(frameReglages, variable = speed, from_ = 1, to = 100, orient = HORIZONTAL, command = getSpeed, label = "Vitesse")
    scaleVitesse.grid(row = 0, column = 0, sticky = "news")




#changement de la couleurs des labels de la Fenetre
def changementFenetre():

    for i in range(0, taille):
        for j in range(0, taille):
            if etatCell[i][j] == True:
                frameJeu.grid_slaves(row = i, column = j)[0].configure(bg = "chartreuse")
            else:
                frameJeu.grid_slaves(row = i, column = j)[0].configure(bg = "light grey")
    #Fenetre.grid_slaves()[]




def compteur(x, y):

    #Compteur de cell vivantes autour de celle aux coordonnées données

    cellVivantesAutour = 0
    for i in range(-1, 2):
        for j in range(-1, 2):

            """
            print(x+i)
            print(y+j)
            print("")
            """

            if x+i >= taille and y+j >= taille:           #En cas de dépassement de la grille, passe à l'autre bout
                if etatCell[x+i - taille][y+j - taille] == True and (i != 0 or j != 0):
                        cellVivantesAutour += 1

            elif x+i >= taille:
                if etatCell[x+i - taille][y+j] == True and (i != 0 or j != 0):
                        cellVivantesAutour += 1

            elif y+j >= taille:
                if etatCell[x+i][y+j - taille] == True and (i != 0 or j != 0):
                        cellVivantesAutour += 1

            elif etatCell[x+i][y+j] == True and (i != 0 or j != 0 ):
                    cellVivantesAutour += 1


    return cellVivantesAutour



"""
def boucle():
    changement()
    remplissageFenetre()
    Fenetre.after(1000, changement)
"""


#mise a jour des cell

def changement():
    global etatCell, etatCell2
    for i in range(0, taille):
        for j in range(0, taille):

            if compteur(i, j) == 3:
                etatCell2[i][j] = True
            elif compteur(i, j) == 2 and etatCell[i][j] == True:
                etatCell2[i][j] = True
            else:
                etatCell2[i][j] = False

    etatCell = etatCell2



def getSpeed(a):
    global pause
    pause = 10/int(a)


def update():
    changement()
    changementFenetre()



def boucle():
    global pause
    update()
    Fenetre.after(int(pause * 1000), boucle) #Attente entre 2 étapes







#initialisation

generation()
initialisationFenetre()




#Lancement programme

boucle()
Fenetre.mainloop()


"""
while True:
    #Fenetre.update_idletasks()
    #Fenetre.update()

    try:
        Fenetre.after(pause*1000, boucle)
        #changement()            #Calcul des changemnet
        #changementFenetre()     #Affichage des changements sur la fenetre
    except TclError:
        #print(sys.exc_info()[0])
        break

    #time.sleep(pause)
"""


print("fini")


#
