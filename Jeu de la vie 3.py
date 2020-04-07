#!/usr/bin/env python3
# -- coding: utf-8 --



# Importation des modules
from tkinter import *
from tkinter.messagebox import *
from random import *
import time
from tkinter.filedialog import *
from tkinter.colorchooser import *
from copy import deepcopy
import os
import numpy as np
from scipy import signal


#Chemin relatif pour les fichiers

fullpath = os.path.abspath(__file__)
os.chdir(os.path.dirname(fullpath))


#Variables

pause = 0.001                   #Temps de pause entre chaque étape (en s)
couleurVivant = "chartreuse"    #Couleur de base pour les cellules vivantes
random = False                  #map générée random
stop = False                    #Pour le bouton start/stop
vide = False                    #Pour créer une map vide
importation = False             #Importation d'une map
etape = 0
genere = False
taille = 20


#Tableau pour compter les cell autour

comparaison = np.full((3,3), 1, dtype=int)
comparaison[1, 1] = 0



#Fenetre Principale
Fenetre = Tk()
Fenetre.title("Jeu de la Vie by Marius")

frameJeu = Frame(Fenetre)
frameJeu.grid(row = 1, column = 1, sticky = "news")


#Commandes boutons

def choixMap():
    global etape, etatCell, contenuFichier, taille, importation

    importation = True
    random = False
    stop = False
    vide = False

    filepath = askopenfilename(title = "Ouvrir une map",filetypes = [
                                    ("txt files", ".txt")])
    print(filepath)
    fichier = open(filepath, "r")      #Importation du fichier map.txt
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne

    try:
        del etatCell
    except NameError:
        pass

    etatCell = np.zeros((taille), dtype=int)
    etape = 0

    resetFrame()


    generation()
    initialisationFenetre()

    frameCommande.grid(columnspan = 3, column = 0)


def choixMoulin():
    global etape, etatCell, contenuFichier, taille, importation

    importation = True
    random = False
    stop = False
    vide = False

    fichier = open("map moulin.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne


    try:
        del etatCell
    except NameError:
        pass

    etatCell = np.zeros((taille), dtype=int)
    etape = 0

    resetFrame()


    generation()
    initialisationFenetre()

    frameCommande.grid(columnspan = 3, column = 0)


def choixRandom():
    global etape, etatCell, contenuFichier, taille, random

    random = True
    importation = True
    stop = False
    vide = False
    taille = int(spinboxTaille.get())

    try:
        del etatCell
    except NameError:
        pass

    etatCell = np.zeros((taille), dtype=int)
    etape = 0

    resetFrame()

    generation()
    initialisationFenetre()

    frameCommande.grid(columnspan = 3, column = 0)


def choixStatique():
    global etape, etatCell, contenuFichier, taille, importation


    importation = True
    random = False
    stop = False
    vide = False

    fichier = open("map statique.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne


    try:
        del etatCell
    except NameError:
        pass

    etatCell = np.zeros((taille), dtype=int)
    etape = 0

    resetFrame()


    generation()
    initialisationFenetre()

    frameCommande.grid(columnspan = 3, column = 0)


def choixClignotant():
    global etape, etatCell, contenuFichier, taille, importation


    importation = True
    random = False
    stop = False
    vide = False

    fichier = open("map clignotant.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne


    try:
        del etatCell
    except NameError:
        pass

    etatCell = np.zeros((taille), dtype=int)
    etape = 0

    resetFrame()


    generation()
    initialisationFenetre()

    frameCommande.grid(columnspan = 3, column = 0)


def choixVaisseau():
    global etape, etatCell, contenuFichier, taille, importation

    importation = True
    random = False
    stop = False
    vide = False

    fichier = open("map vaisseau.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne


    try:
        del etatCell
    except NameError:
        pass

    etatCell = np.zeros((taille), dtype=int)
    etape = 0

    resetFrame()


    generation()
    initialisationFenetre()

    frameCommande.grid(columnspan = 3, column = 0)




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
    fichierEcriture = asksaveasfile(title = "Enregistrer la configuration actuelle", filetypes = [
                                            ("txt files", ".txt")])
    texteEcriture = str(taille) + "\n"

    for x in range(taille):
        for y in range(taille):
            if etatCell[y, x] == 1:
                texteEcriture += "1"
            elif etatCell[y, x] == 0:
                texteEcriture += "0"
        texteEcriture += "\n"

    fichierEcriture.write(texteEcriture)
    fichierEcriture.close()


def creerGrilleVide():
    global etape, taille, vide, etatCell, importation

    importation = False
    random = False
    stop = False
    vide = True
    taille = int(spinboxTaille.get())


    try:
        del etatCell
    except NameError:
        pass

    etatCell = np.zeros((taille), dtype=int)
    etape = 0

    resetFrame()


    generation()
    initialisationFenetre()

    frameCommande.grid(columnspan = 3, column = 0)


def changerCouleur():
    global couleurVivant

    couleurVivantTemp = askcolor()[1]
    if couleurVivantTemp != None:
        couleurVivant = couleurVivantTemp

    actualisationFenetre()



#Génération

def generation():
    global pourcentageVivant, genere, etatCell

    genere = True

    Fenetre.rowconfigure(0, pad = 5, minsize = 100)
    Fenetre.rowconfigure(1, weight = 1, pad = 5, minsize = 100)
    Fenetre.rowconfigure(2, pad = 5, minsize = 100)

    Fenetre.columnconfigure(1, weight = 1, pad = 5, minsize = 50)

    for y in range(taille):

        frameJeu.columnconfigure(y, weight = 1)  #Pour éviter la déformation
        frameJeu.rowconfigure(y, weight = 1)     #en étirant la fenetre


    if vide == True:
        etatCell = np.zeros((taille, taille), dtype=int)


    if random == True:
        etatCell = np.random.randint(0, 2, size = [taille, taille])

    if importation == True:
        mapFichier = contenuFichier.split("\n")     #Tableau de la map
                                                    #1 ligne sur le txt = 1 ligne du jeu
        etatCell = np.zeros((taille, taille), dtype=int)

        for x in range(taille):
            for y in range(taille):

                if mapFichier[y + 1][x] == "0":       #0 sur txt = morte
                    etatCell[y, x] = 0

                elif mapFichier[y + 1][x] == "1":     #1 sur txt = vivante
                    etatCell[y, x] = 1

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
            if etatCell[y, x] == 1:          #Si cell vivante
                Label(frameJeu,                  #case verte (ou couleur choisie)
                    text = "   ",
                    relief = GROOVE,
                    borderwidth = 1,
                    bg = couleurVivant).grid(
                    row = y, column = x, sticky = "news")

            elif etatCell[y, x] == 0:       #Si cell morte
                Label(frameJeu,                  #case grise
                    text = "   ",
                    relief = GROOVE,
                    borderwidth = 1,
                    bg = "light grey").grid(
                    row = y, column = x, sticky = "news")

            else:
                print("Erreur Cell ni vivante ni morte")    #Erreur, pas censé arriver

    nombreCell["text"] = str(np.sum(etatCell)) + " Cellules vivantes"


def etapeSuivante():
    global etatCell

    mapCompteur = signal.convolve2d(etatCell, comparaison, mode = "same", boundary = "wrap")

    etatCell = ((((mapCompteur == 3).astype(int) * 2) + (mapCompteur == 2).astype(int) + (etatCell == 1).astype(int)) >= 2).astype(int)




def actualisationFenetre():

    for x in range(taille):
        for y in range(taille):
            if etatCell[y, x] == 1:
                frameJeu.grid_slaves(row = y, column = x)[0].configure(bg = couleurVivant)

            else:
                frameJeu.grid_slaves(row = y, column = x)[0].configure(bg = "light grey")




def changement():

    etapeSuivante()
    actualisationFenetre()


def resetFrame():       #Clear la frame pour en remettre une autre
    for widget in frameJeu.winfo_children():
        widget.grid_forget()

    nombreEtapes["text"] = "Étape : 0"
    nombreCell["text"] = str(np.sum(etatCell)) + " Cellules vivantes"



antistart = 0

def bouclePrincipale():
    global antistart, pause, stop, etape

    if antistart == 1 and stop == False:
        changement()
        etape += 1
        nombreEtapes["text"] = "Étape : " + str(etape)

    nombreCell["text"] = str(np.sum(etatCell)) + " Cellules vivantes"
    antistart = 1

    Fenetre.after(int(pause * 1000), bouclePrincipale)




#Clique gauche pour modification de la map


def action(event):

    if event.type != "" and event.num == 1 and genere == True and type(event.widget) != Tk:

        position = event.widget.grid_info()

        if event.widget["bg"] == "light grey" and event.widget["text"] == "   ":
            event.widget["bg"] = couleurVivant
            etatCell[position["row"], position["column"]] = 1

        elif event.widget["bg"] == couleurVivant and event.widget["text"] == "   ":
            event.widget["bg"] = "light grey"
            etatCell[position["row"], position["column"]] = 0



#Clique gauche event
Fenetre.bind("<ButtonPress-1>", action)


#Commandes

frameCommande = LabelFrame(Fenetre, text = "Commandes")
frameCommande.grid(row = 0, column = 1, sticky = "news")


boutonStart = Button(frameCommande, text = "Start", fg = "chartreuse", command = start)
boutonStart.grid(row = 0, column = 0)

boutonSave = Button(frameCommande, text = "Save", command = save)
boutonSave.grid(row = 0, column = 1)

labelTaille = Label(frameCommande, text = " Taille =")
labelTaille.grid(row = 0, column = 2)

spinboxTaille = Spinbox(frameCommande, from_ = 1, to = 50)
spinboxTaille.grid(row = 0, column = 3)

boutonGrille = Button(frameCommande, text = "Créer une grille vide", command = creerGrilleVide)
boutonGrille.grid(row = 0, column = 4)

boutonCouleur = Button(frameCommande, text = "Changer la couleur des cellules vivantes", command = changerCouleur)
boutonCouleur.grid(row = 0, column = 5)


#Infos

frameInfos = LabelFrame(Fenetre, text = "Infos")
frameInfos.grid(row = 2, column = 1, sticky = "news")

nombreEtapes = Label(frameInfos, text = "Étape 0")
nombreEtapes.pack()

nombreCell = Label(frameInfos, text = "0 Cellules Vivantes")
nombreCell.pack()

#Lancement

Fenetre.mainloop()


#
