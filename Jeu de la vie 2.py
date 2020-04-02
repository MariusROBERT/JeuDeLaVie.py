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


#Chemin relatif pour les fichiers

fullpath = os.path.abspath(__file__)
os.chdir(os.path.dirname(fullpath))


#Variables
#taille = 10                     #Taille d'un côté de la map (carré)
pourcentageVivant = 50
etatCell = []                   #map avec état cell à l'étape n
etatCell2 = []                  #map avec état cell à l'étape n+1
pause = 0.001                   #Temps de pause entre chaque étape (en s)
couleurVivant = "chartreuse"    #Couleur de base pour les cellules vivantes
random = False                  #map générée random
stop = False                    #Pour le bouton start/stop
vide = False                    #Pour créer une map vide
importation = False             #Importation d'une map
etape = 0
genere = False



#Fenetre Principale
Fenetre = Tk()
Fenetre.title("Jeu de la Vie by Marius")

frameJeu = Frame(Fenetre)
frameJeu.grid(row = 1, column = 1, sticky = "news")


#Commandes boutons

def choixMap():
    global etape, etatCell, etatCell2, contenuFichier, taille, importation

    del etatCell
    del etatCell2
    etatCell = []
    etatCell2 = []
    etape = 0

    resetFrame()

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
    print(taille)

    generation()
    initialisationFenetre()

    frameCommande.grid(columnspan = 3, column = 0)


def choixMoulin():
    global etape, etatCell, etatCell2, contenuFichier, taille, importation

    del etatCell
    del etatCell2
    etatCell = []
    etatCell2 = []
    etape = 0

    resetFrame()

    importation = True
    random = False
    stop = False
    vide = False

    fichier = open("map moulin.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne
    print(taille)

    generation()
    initialisationFenetre()

    frameCommande.grid(columnspan = 3, column = 0)


def choixRandom():
    global etape, etatCell, etatCell2, contenuFichier, taille, random

    del etatCell
    del etatCell2
    etatCell = []
    etatCell2 = []
    etape = 0

    resetFrame()

    random = True
    importation = True
    stop = False
    vide = False

    generation()
    initialisationFenetre()

    frameCommande.grid(columnspan = 3, column = 0)


def choixStatique():
    global etape, etatCell, etatCell2, contenuFichier, taille, importation

    del etatCell
    del etatCell2
    etatCell = []
    etatCell2 = []
    etape = 0

    resetFrame()

    importation = True
    random = False
    stop = False
    vide = False

    fichier = open("map statique.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne
    print(taille)

    generation()
    initialisationFenetre()

    frameCommande.grid(columnspan = 3, column = 0)


def choixClignotant():
    global etape, etatCell, etatCell2, contenuFichier, taille, importation

    del etatCell
    del etatCell2
    etatCell = []
    etatCell2 = []
    etape = 0

    resetFrame()

    importation = True
    random = False
    stop = False
    vide = False

    fichier = open("map clignotant.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne
    print(taille)

    generation()
    initialisationFenetre()

    frameCommande.grid(columnspan = 3, column = 0)


def choixVaisseau():
    global etape, etatCell, etatCell2, contenuFichier, taille, importation

    del etatCell
    del etatCell2
    etatCell = []
    etatCell2 = []
    etape = 0

    resetFrame()

    importation = True
    random = False
    stop = False
    vide = False

    fichier = open("map vaisseau.txt", "r")
    contenuFichier = fichier.read()
    fichier.close()

    taille = int(contenuFichier.split("\n")[0])     #Taille de la map sur la 1ère ligne
    print(taille)

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
            if etatCell[y][x] == True:
                texteEcriture += "1"
            elif etatCell[y][x] == False:
                texteEcriture += "0"
        texteEcriture += "\n"

    fichierEcriture.write(texteEcriture)
    fichierEcriture.close()


def creerGrilleVide():
    global etape, taille, vide, etatCell, etatCell2, importation

    del etatCell
    del etatCell2
    etatCell = []
    etatCell2 = []
    etape = 0

    resetFrame()

    importation = False
    random = False
    stop = False
    vide = True
    taille = int(spinboxTaille.get())

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
    global pourcentageVivant, genere

    genere = True

    Fenetre.rowconfigure(0, pad = 5, minsize = 100)
    Fenetre.rowconfigure(1, weight = 1, pad = 5, minsize = 100)
    Fenetre.rowconfigure(2, pad = 5, minsize = 100)

    Fenetre.columnconfigure(1, weight = 1, pad = 5, minsize = 50)

    for y in range(taille):
        etatCell.append([])     #Tableaux
        etatCell2.append([])

        frameJeu.columnconfigure(y, weight = 1)  #Pour éviter la déformation
        frameJeu.rowconfigure(y, weight = 1)     #en étirant la fenetre

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
                Label(frameJeu,                  #case verte (ou couleur choisie)
                    text = "   ",
                    relief = GROOVE,
                    borderwidth = 1,
                    bg = couleurVivant).grid(
                    row = y, column = x, sticky = "news")

            elif etatCell[y][x] == False:       #Si cell morte
                Label(frameJeu,                  #case grise
                    text = "   ",
                    relief = GROOVE,
                    borderwidth = 1,
                    bg = "light grey").grid(
                    row = y, column = x, sticky = "news")

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



antistart = 0

def bouclePrincipale():
    global antistart, pause, stop, etape

    if antistart == 1 and stop == False:
        changement()
        etape += 1
        nombreEtapes["text"] = "Étape : " + str(etape)

    antistart = 1

    Fenetre.after(int(pause * 1000), bouclePrincipale)




#Clique gauche pour modification de la map


def action(event):

    if event.type != "" and event.num == 1 and genere == True and type(event.widget) != Tk:

        position = event.widget.grid_info()

        if event.widget["bg"] == "light grey" and event.widget["text"] == "   ":
            event.widget["bg"] = couleurVivant
            etatCell[position["row"]][position["column"]] = True

        elif event.widget["bg"] == couleurVivant and event.widget["text"] == "   ":
            event.widget["bg"] = "light grey"
            etatCell[position["row"]][position["column"]] = False



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


#Lancement

Fenetre.mainloop()

print("FIN")

#
