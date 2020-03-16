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
taille = 25
pourcentageVivant = 50
etatCell = []                   #map avec état cell à l'étape n
etatCell2 = []                  #map avec état cell à l'étape n+1
pause = 0.01                    #Temps de pause entre chaue étape (en s)
random = False                  #map random ou via fichier
choixCouleur = False            #choixCouleur ou couleur de base
couleurVivant = "chartreuse"
stop = False                    #Pour le bouton start/stop
vide = False                    #Pour créer une map vide
importation = False             #Importation d'une map



#Fenetre Principale
Fenetre = Tk()
Fenetre.title("Jeu de la Vie by Marius")



#Options

if choixCouleur == True:
    couleurVivant = (tkinter.colorchooser.askcolor(color=None))[1]



#Commandes boutons


def choixMap():
    global contenuFichier, taille, importation

    importation = True

    filepath = askopenfilename(title = "Ouvrir une map",filetypes = [("txt files", ".txt")])
    print(filepath)
    fichier = open(filepath, "r")      #Importation du fichier map.txt
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne
    print(taille)

    generation()
    initialisationFenetre()

    frame.grid(columnspan = taille)


def choixMoulin():
    global contenuFichier, taille, importation

    importation = True

    fichier = open("map moulin.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne
    print(taille)

    generation()
    initialisationFenetre()

    frame.grid(columnspan = taille)


def choixRandom():
    global contenuFichier, taille, random

    random = True

    generation()
    initialisationFenetre()

    frame.grid(columnspan = taille)


def choixStatique():
    global contenuFichier, taille, importation

    importation = True

    fichier = open("map statique.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne
    print(taille)

    generation()
    initialisationFenetre()

    frame.grid(columnspan = taille)


def choixClignotant():
    global contenuFichier, taille, importation

    importation = True

    fichier = open("map clignotant.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne
    print(taille)

    generation()
    initialisationFenetre()

    frame.grid(columnspan = taille)


def choixVaisseau():
    global contenuFichier, taille, importation

    importation = True

    fichier = open("map vaisseau.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne
    print(taille)

    generation()
    initialisationFenetre()

    frame.grid(columnspan = taille)




def start():
    global stop

    stop = False

    boutonStart.config(text = "Stop", fg = "red", command = stopBoucle)

    if antistart == 0:          #Lance la boucle la première fois
        bouclePrincipale()      #Les autres fois, change juste stop à False et aspect du bouton


def stopBoucle():
    global stop

    stop = True

    boutonStart.config(text = "Start", fg = "chartreuse", command = start)


def save():
    fichierEcriture = asksaveasfile(title = "Enregistrer la configuration actuelle", filetypes = [("txt files", ".txt")])
    texteEcriture = str(taille) + "\n"

    for x in range(taille):
        for y in range(taille):
            if etatCell[y][x] == True:
                texteEcriture += "1"
            elif etatCell[y][x] == False:
                texteEcriture += "0"
        texteEcriture += "\n"

    fichierEcriture.write(texteEcriture)
    fichierEcriture.close()


def creerGrille():
    global taille, vide

    vide = True
    taille = int(spinboxTaille.get())

    generation()
    initialisationFenetre()

    frame.grid(columnspan = taille)


#Génération

def generation():
    global pourcentageVivant, genere

    genere = True

    Fenetre.columnconfigure(0, weight = 1)
    Fenetre.rowconfigure(0, weight = 1)

    for y in range(taille):
        etatCell.append([])     #Tableaux
        etatCell2.append([])

        Fenetre.columnconfigure(y + 1, weight = 1)  #Pour éviter la déformation
        Fenetre.rowconfigure(y + 1, weight = 1)     #en étirant la fenetre

        for x in range(taille):
            etatCell[y].append([])  #Double tableaux
            etatCell2[y].append([])

            if random == True:

                if randint(0, 100) < pourcentageVivant:     #Remplissage aléatoire
                    etatCell[y][x] = True                   #de la map en fonction
                else:                                       #du pourcentage choisi
                    etatCell[y][x] = False

            if vide == True:
                etatCell[y][x] = False


    if importation == True:
        mapFichier = contenuFichier.split("\n")     #Tableau de la map
                                                    #1 ligne sur le txt
        for x in range(taille):                     #-> 1 case du tableau
            for y in range(taille):

                if mapFichier[y + 1][x] == "0":       #0 sur txt = morte
                    etatCell[y][x] = False

                elif mapFichier[y + 1][x] == "1":     #1 sur txt = vivante
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



antistart = 0

def bouclePrincipale():
    global antistart, pause, stop

    if antistart == 1 and stop == False:
        changement()

    antistart = 1

    Fenetre.after(int(pause * 1000), bouclePrincipale)


#Clique gauche pour modification de la map


def action(event):

    if event.type != "" and event.num == 1:

        position = event.widget.grid_info()

        if event.widget["bg"] == "light grey" and event.widget["text"] == "   ":
            event.widget["bg"] = couleurVivant
            etatCell[position["row"] - 1][position["column"]] = True

        elif event.widget["bg"] == couleurVivant and event.widget["text"] == "   ":
            event.widget["bg"] = "light grey"
            etatCell[position["row"] - 1][position["column"]] = False



#Clique gauche event
Fenetre.bind("<ButtonPress-1>", action)


#Commandes

frame = LabelFrame(Fenetre, text = "Commandes")
frame.grid(row = 0, column = 0)


boutonStart = Button(frame, text = "Start", fg = "chartreuse", command = start, borderwidth = 10)
boutonStart.grid(row = 0, column = 0)

boutonSave = Button(frame, text = "Save", command = save, borderwidth = 10)
boutonSave.grid(row = 0, column = 1)

labelTaille = Label(frame, text = " Taille =")
labelTaille.grid(row = 0, column = 2)

spinboxTaille = Spinbox(frame, from_ = 1, to = 50)
spinboxTaille.grid(row = 0, column = 3)

boutonGrille = Button(frame, text = "Créer une grille vide", command = creerGrille)
boutonGrille.grid(row = 0, column = 4)


#Lancement

Fenetre.mainloop()

print("FIN")

#
