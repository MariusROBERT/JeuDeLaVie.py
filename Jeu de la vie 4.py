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
cote_case = 10


cases = {}

#Tableau pour compter les cell autour

comparaison = np.full((3,3), 1, dtype=int)
comparaison[1, 1] = 0



#Fenetre Principale
Fenetre = Tk()
Fenetre.title("Jeu de la Vie by Marius")

frameJeu = Frame(Fenetre)
frameJeu.grid(row = 1, column = 1, sticky = "news")

grille_jeu = Canvas(frameJeu,
                    width=cote_case*(taille)+5,
                    height=cote_case*(taille)+5,
                    background="light grey", cursor="gumby")

grille_jeu.pack()

#Commandes boutons

def choixMap():
    global etape, etatCell, contenuFichier, taille, importation

    importation = True
    random = False
    stopBoucle()
    vide = False

    filepath = askopenfilename(title = "Ouvrir une map",filetypes = [
                                    ("txt files", ".txt")])
    print(filepath)
    try:
        fichier = open(filepath, "r")      #Importation du fichier map.txt
        contenuFichier = fichier.read()
        fichier.close()

        taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne


        try:
            del etatCell
        except NameError:
            pass

        etatCell = np.zeros((taille, taille), dtype=int)
        etape = 0

        resetFrame()


        generation()
        initialisationFenetre()

        frameCommande.grid(columnspan = 3, column = 0)

    except FileNotFoundError:
        pass

def choixMoulin():
    global etape, etatCell, contenuFichier, taille, importation

    importation = True
    random = False
    stopBoucle()
    vide = False

    fichier = open("map moulin.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne


    try:
        del etatCell
    except NameError:
        pass

    etatCell = np.zeros((taille, taille), dtype=int)
    etape = 0

    resetFrame()


    generation()
    initialisationFenetre()

    frameCommande.grid(columnspan = 3, column = 0)


def choixRandom():
    global etape, etatCell, contenuFichier, taille, random

    random = True
    importation = False
    stopBoucle()
    vide = False
    taille = int(spinboxTaille.get())

    try:
        del etatCell
    except NameError:
        pass

    etatCell = np.zeros((taille, taille), dtype=int)
    etape = 0

    resetFrame()

    generation()
    initialisationFenetre()

    frameCommande.grid(columnspan = 3, column = 0)


def choixStatique():
    global etape, etatCell, contenuFichier, taille, importation


    importation = True
    random = False
    stopBoucle()
    vide = False

    fichier = open("map statique.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne


    try:
        del etatCell
    except NameError:
        pass

    etatCell = np.zeros((taille, taille), dtype=int)
    etape = 0

    resetFrame()


    generation()
    initialisationFenetre()

    frameCommande.grid(columnspan = 3, column = 0)


def choixClignotant():
    global etape, etatCell, contenuFichier, taille, importation


    importation = True
    random = False
    stopBoucle()
    vide = False

    fichier = open("map clignotant.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne


    try:
        del etatCell
    except NameError:
        pass

    etatCell = np.zeros((taille, taille), dtype=int)
    etape = 0

    resetFrame()


    generation()
    initialisationFenetre()

    frameCommande.grid(columnspan = 3, column = 0)


def choixVaisseau():
    global etape, etatCell, contenuFichier, taille, importation

    importation = True
    random = False
    stopBoucle()
    vide = False

    fichier = open("map vaisseau.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne


    try:
        del etatCell
    except NameError:
        pass

    etatCell = np.zeros((taille, taille), dtype=int)
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
    stopBoucle()

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
    global etape, taille, vide, etatCell, importation, random

    importation = False
    random = False
    stopBoucle()
    vide = True
    taille = int(spinboxTaille.get())


    try:
        del etatCell
    except NameError:
        pass

    etatCell = np.zeros((taille, taille), dtype=int)
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

    grille_jeu.config(height=cote_case*(taille)+5,
                        width=cote_case*(taille)+5,)

    for x in range(taille):
        for y in range(taille):
            if etatCell[y, x] == 1:          #Si cell vivante
                cases[(x, y)] = grille_jeu.create_rectangle(cote_case*x+5, cote_case*y+5, cote_case *(x+1)+5, cote_case*(y+1)+5,
                                                            fill=couleurVivant, activefill="#4e8517", tags=(x, y))

            elif etatCell[y, x] == 0:       #Si cell morte
                cases[(x, y)] = grille_jeu.create_rectangle(cote_case*x+5, cote_case*y+5, cote_case *(x+1)+5, cote_case*(y+1)+5,
                                                            fill="light grey", activefill="dark grey", tags=(x, y))

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
                grille_jeu.itemconfig(grille_jeu.find_withtag(cases[(x, y)])[0], fill=couleurVivant)
            else:
                grille_jeu.itemconfig(grille_jeu.find_withtag(cases[(x, y)])[0], fill="light grey")




def changement():

    etapeSuivante()
    actualisationFenetre()


def resetFrame():       #Clear la frame pour en remettre une autre
    grille_jeu.addtag_all("reset")
    grille_jeu.delete("reset")


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

def click(event):
    if type(event.widget) != Tk:
        tags = grille_jeu.itemconfig(grille_jeu.find_closest(event.x, event.y)[0])["tags"][4].split()
        if (grille_jeu.itemconfig(grille_jeu.find_closest(event.x, event.y)[0])["fill"][4]) == "light grey":
            etatCell[int(tags[1]), int(tags[0])] = True
            grille_jeu.itemconfig(grille_jeu.find_closest(event.x, event.y)[0], fill=couleurVivant, activefill="#4e8517")

        elif (grille_jeu.itemconfig(grille_jeu.find_closest(event.x, event.y)[0])["fill"][4]) == couleurVivant:
            etatCell[int(tags[1]), int(tags[0])] = False
            grille_jeu.itemconfig(grille_jeu.find_closest(event.x, event.y)[0], fill="lightgrey", activefill="dark grey")





#Clique gauche event
grille_jeu.bind("<ButtonPress-1>", click)


#Commandes

frameCommande = LabelFrame(Fenetre, text = "Commandes")
frameCommande.grid(row = 0, column = 1, sticky = "news")


boutonStart = Button(frameCommande, text = "Start", fg = "chartreuse", command = start)
boutonStart.grid(row = 0, column = 0)

boutonSave = Button(frameCommande, text = "Save", command = save)
boutonSave.grid(row = 0, column = 1)

labelTaille = Label(frameCommande, text = " Taille =")
labelTaille.grid(row = 0, column = 2)

spinboxTaille = Spinbox(frameCommande, from_ = 1, to = 50, textvariable=DoubleVar(value=20))
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
creerGrilleVide()

bouclePrincipale()
Fenetre.mainloop()


#
