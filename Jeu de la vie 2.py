#!/usr/bin/env python3
# -- coding: utf-8 --



# Importation des modules
from tkinter import *
from tkinter.messagebox import *
from random import *
import time
from tkinter.filedialog import *
import tkinter.colorchooser
from copy import deepcopy
import os


#Chemin relatif pour les fichiers

fullpath = os.path.abspath(__file__)
os.chdir(os.path.dirname(fullpath))


#Variables
taille = 5
pourcentageVivant = 20
etatCell = []               #map avec état cell à l'étape n
etatCell2 = []              #map avec état cell à l'étape n+1
pause = 0.5                 #Temps de pause entre chaue étape (en s)
random = False              #map random ou via fichier
choixCouleur = False        #choixCouleur ou couleur de base
couleurVivant = "chartreuse"
stop = False



#Fenetre Principale
Fenetre = Tk()
Fenetre.title("Jeu de la Vie by Marius")



#Options

if choixCouleur == True:
    couleurVivant = (tkinter.colorchooser.askcolor(color=None))[1]



#Commandes boutons


def choixMap():
    global contenuFichier, taille

    random = False

    filepath = askopenfilename(title = "Ouvrir une map",filetypes = [("txt files", ".txt")])
    print(filepath)
    fichier = open(filepath, "r")      #Importation du fichier map.txt
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne
    print(taille)

    generation()
    initialisationFenetre()


def choixMoulin():
    global contenuFichier, taille

    random = False

    fichier = open("map moulin.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne
    print(taille)

    generation()
    initialisationFenetre()


def choixRandom():
    global contenuFichier, taille

    random = True

    generation()
    initialisationFenetre()


def choixStatique():
    global contenuFichier, taille

    random = False

    fichier = open("map statique.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne
    print(taille)

    generation()
    initialisationFenetre()


def choixClignotant():
    global contenuFichier, taille

    random = False

    fichier = open("map clignotant.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne
    print(taille)

    generation()
    initialisationFenetre()


def choixVaisseau():
    global contenuFichier, taille

    random = False

    fichier = open("map vaisseau.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne
    print(taille)

    generation()
    initialisationFenetre()




def start():
    global stop

    print("start")
    stop = False

    boutonStart.config(text = "Stop", fg = "red", command = stopBoucle)

    if test == 0:
        bouclePrincipale()


def stopBoucle():
    global stop

    print("stop")
    stop = True

    boutonStart.config(text = "Start", fg = "chartreuse", command = start)



#Génération

def generation():
    global pourcentageVivant


    for y in range(taille):
        etatCell.append([])     #Tableaux
        etatCell2.append([])

        Fenetre.columnconfigure(y, weight = 1)  #Pour éviter la déformation
        Fenetre.rowconfigure(y, weight = 1)     #en étirant la fenetre

        for x in range(taille):
            etatCell[y].append([])  #Double tableaux
            etatCell2[y].append([])

            if random == True:

                if randint(0, 100) < pourcentageVivant:     #Remplissage aléatoire
                    etatCell[y][x] = True                   #de la map en fonction
                else:                                       #du pourcentage choisi
                    etatCell[y][x] = False

    if random == False:
        mapFichier = contenuFichier.split("\n")     #Tableau de la map
                                                    #1 ligne sur le txt
        for x in range(taille):                     #-> 1 case du tableau
            for y in range(taille):

                if mapFichier[y+1][x] == "0":       #0 sur txt = morte
                    etatCell[y][x] = False

                elif mapFichier[y+1][x] == "1":     #1 sur txt = vivante
                    etatCell[y][x] = True

#Barre de menus

menubar = Menu(Fenetre)
Fenetre.config(menu = menubar)

menuMap = Menu(menubar, tearoff = 0)                            #menu des map préconfig
menubar.add_cascade(label = "Configuration", menu = menuMap)

menuMap.add_command(label = "Random", command = choixRandom)
menuMap.add_command(label = "Moulin", command = choixMoulin)
menuMap.add_command(label = "Clignotant", command = choixClignotant)
menuMap.add_command(label = "Statique", command = choixStatique)
menuMap.add_command(label = "Vaisseau", command = choixVaisseau)
menuMap.add_separator()
menuMap.add_command(label = "Importer map", command = choixMap)








#Fenetre

def initialisationFenetre():

    for x in range(taille):
        for y in range(taille):
            if etatCell[y][x] == True:          #Si cell vivante
                Label(Fenetre,                  #case verte (ou couleur choisie)
                    text = "   ",
                    relief = GROOVE,
                    borderwidth = 1,
                    bg = couleurVivant).grid(
                    row = y + 1, column = x, sticky = "news")

            elif etatCell[y][x] == False:       #Si cell morte
                Label(Fenetre,                  #case grise
                    text = "   ",
                    relief = GROOVE,
                    borderwidth = 1,
                    bg = "light grey").grid(
                    row = y + 1, column = x, sticky = "news")

            else:
                print("Erreur Cell ni vivante ni morte")    #Erreur, pas censé arriver


def compteur(x, y):

    cellVivantesAutour = 0

    for yadd in range(-1, 2):       #Ligne au dessus, même ligne et ligne en dessous
        for xadd in range(-1, 2):   #Pareil pour colonnes

            yfinal = y + yadd
            xfinal = x + xadd

            if yfinal >= taille and xfinal >= taille:       #Si dépasse de la map x & y, reviens de l'autre côté
                if etatCell[yfinal - taille][xfinal - taille] == True:
                    cellVivantesAutour += 1

            elif yfinal >= taille:                          #Si dépasse de la map en y, reviens de l'autre côté
                if etatCell[yfinal - taille][xfinal] == True:
                    cellVivantesAutour += 1

            elif xfinal >= taille:                          #Si dépasse de la map en x, reviens de l'autre côté
                if etatCell[yfinal][xfinal - taille] == True:
                    cellVivantesAutour += 1

            elif yadd != 0 or xadd != 0:                    #On compte les cases autour mais pas la case elle même
                if etatCell[yfinal][xfinal] == True:
                    cellVivantesAutour += 1

            elif yadd == 0 and xadd == 0:
                pass

    return cellVivantesAutour


def etapeSuivante():
    global etatCell, etatCell2


    for x in range(taille):
        for y in range(taille):

            cellVivantesAutour = compteur(x, y)

            if cellVivantesAutour == 3:
                etatCell2[y][x] = True

            elif cellVivantesAutour == 2 and etatCell[y][x] == True:
                etatCell2[y][x] = True

            else:
                etatCell2[y][x] = False

    etatCell = deepcopy(etatCell2)



def actualisationFenetre():

    for x in range(taille):
        for y in range(taille):
            if etatCell[y][x] == True:
                Fenetre.grid_slaves(row = y + 1, column = x)[0].configure(bg = couleurVivant)

            else:
                Fenetre.grid_slaves(row = y + 1, column = x)[0].configure(bg = "light grey")




def changement():



    etapeSuivante()
    actualisationFenetre()


test = 0


def bouclePrincipale():
    global test, pause, stop

    if test == 1 and stop == False:
        changement()

    test = 1

    Fenetre.after(int(pause * 1000), bouclePrincipale)


#Bouton start/stop

boutonStart = Button(Fenetre, text = "Start", fg = "chartreuse", command = start, borderwidth = 10)
boutonStart.grid(row = 0, column = 0, columnspan = taille)


#Lancement

Fenetre.mainloop()

print("fin")

#
