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
pause = 3
random = False



if random == False:
    fichier = open("map.txt", "r")      #Importation du fichier map.txt
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])
    print(taille)
    #print(contenuFichier)




#Fenetre Principale
Fenetre = Tk()
Fenetre.title("Jeu de la Vie by Marius")



#Génération

def generation():

    #mise en place du tableau et remplissage des cell vivantes et mortes

    for i in range(taille):
        etatCell.append([])
        etatCell2.append([])
        Fenetre.columnconfigure(i, weight = 1)
        Fenetre.rowconfigure(i, weight = 1)
        #print(str(i) + "  i")

        for j in range(taille):
            etatCell[i].append([])      #Double tableaux de coordonnées [x][y] avec True/False pour état cell
            etatCell2[i].append([])
            #print(str(j) + "  j")

            if random == True:
                if randint(0, 100) < pourcentageVivant: #Remplissage du tableau True/False avec le pourcentage donné
                    etatCell[i][j] = True
                else:
                    etatCell[i][j] = False


    if random == False:

        #for i in range(len(contenuFichier)):

        mapFichier = contenuFichier.split("\n")


        for i in range(taille):
            print(mapFichier[i+1])
            for j in range(taille):
                if mapFichier[i+1][j] == "0":    #0 = cell morte
                    etatCell[i][j] = False
                    #print("mort")

                elif mapFichier[i+1][j] == "1":  #1 = cell vivante
                    etatCell[i][j] = True
                    #print("Vivante")



#Fenetre

def initialisationFenetre():
    global speed
    #Création de la fenetre avec case vertes si cell vivante et case grise si cell morte


    for i in range(taille):
        for j in range(taille):
            if etatCell[i][j] == True:
                Label(Fenetre, text = "   ", relief = GROOVE, borderwidth = 1, bg = "chartreuse").grid(row = i, column = j, sticky = "news")
                print("ON")
            else:
                Label(Fenetre, text = "   ", relief = GROOVE, borderwidth = 1, bg = "light grey").grid(row = i, column = j, sticky = "news")
                print("OFF")


    #Slider de vitesse
    speed = IntVar()
    speed = 100
    scaleVitesse = Scale(Fenetre, variable = speed, from_ = 1, to = 100, orient = HORIZONTAL, command = getSpeed, label = "Vitesse")
    scaleVitesse.grid(row = taille, column = 0, columnspan = taille, sticky = "news")




#changement de la couleurs des labels de la Fenetre
def changementFenetre():

    for i in range(taille):
        for j in range(taille):
            if etatCell[i][j] == True:
                Fenetre.grid_slaves(row = i, column = j)[0].configure(bg = "chartreuse")
                #print("ON 2")
            else:
                Fenetre.grid_slaves(row = i, column = j)[0].configure(bg = "light grey")
                #print("OFF 2")
    #Fenetre.grid_slaves()[]




def compteur(x, y):

    #Compteur de cell vivantes autour de celle aux coordonnées données

    cellVivantesAutour = 0
    for j in range(-1, 2):
        #print(i)
        for i in range(-1, 2):

            if x+i >= taille and y+j >= taille:     #En cas de dépassement de la grille, passe à l'autre bout
                if etatCell[x+i - taille][y+j - taille] == True:
                        cellVivantesAutour += 1

            elif x+i >= taille:
                if etatCell[x+i - taille][y+j] == True:
                        cellVivantesAutour += 1

            elif y+j >= taille:
                if etatCell[x+i][y+j - taille] == True:
                        cellVivantesAutour += 1

            elif etatCell[x+i][y+j] == True and (i != 0 or j != 0 ):
                    cellVivantesAutour += 1


    return cellVivantesAutour


#mise a jour des cell

def changement():
    global etatCell, etatCell2
    for i in range(taille):
        for j in range(taille):
            print(str(i) + str("  ") + str(j))
            print(compteur(i, j))
            print(etatCell[i][j])
            if compteur(i, j) == 3:
                etatCell2[i][j] = True
                print("nait")
            elif compteur(i, j) == 2 and etatCell[i][j] == True:
                etatCell2[i][j] = True
                print("persiste")
            else:
                etatCell2[i][j] = False
                print("meurt")
            print()

    """
    print(compteur(1, 2))
    print(etatCell[1][2])
    print(etatCell2[1][2])
    """

    etatCell = etatCell2



def getSpeed(a):
    global pause
    pause = int(10/int(a))


def update():
    changement()
    changementFenetre()

test = 0

def boucle():
    global pause, test

    if test == 1:
        update()
        for i in range(taille):
            print(etatCell[i])
    test = 1
    print(compteur(3,1))
    print(etatCell[1][3])
    Fenetre.after(pause * 1000, boucle) #Attente entre 2 étapes




#Initialisation

generation()
initialisationFenetre()


#Lancement


for i in range(taille):
    print(etatCell[i])



#Lancement programme
time.sleep(10)

boucle()
Fenetre.mainloop()


print("fin")


#
