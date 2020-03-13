#!/usr/bin/env python3
# -- coding: utf-8 --



# Importation des modules
from tkinter import *
from tkinter.messagebox import *
from random import *
import time
import tkinter.colorchooser



#Variables
taille = 10
pourcentageVivant = 17
etatCell = {}  #dico map avec état cell à l'étape n
etatCell2 = {}  #dico map avec état cell à l'étape n+1
pause = 1
random = False
choixCouleur = False
couleurVivant = "chartreuse"


#Fenetre Principale
Fenetre = Tk()
Fenetre.title("Jeu de la Vie by Marius")


#Choix couleur
if choixCouleur == True:
    couleurVivant = (tkinter.colorchooser.askcolor(color=None))[1]


#Génération


def generation():
    global pourcentageVivant

    #print("Generation")

    for x in range(taille):
        for y in range(taille):

            if randint(0, 100) < pourcentageVivant:
                etatCell[x, y] = True
            else:
                etatCell[x, y] = False


#Fenetre


def initialisationFenetre():

    #print("initialisationFenetre")

    for x in range(taille):
        for y in range(taille):
            if etatCell.get(x, y) == True:
                Label(
                    Fenetre,
                    text = "     ",
                    relief = GROOVE,
                    borderwidth = 1,
                    bg = couleurVivant).grid(row = y, column = x, sticky = "news")
            else:
                Label(
                    Fenetre,
                    text = "     ",
                    relief = GROOVE,
                    borderwidth = 1,
                    bg = "light grey").grid(row = y, column = x, sticky = "news")


def compteur(x, y):

    #print("compteur")

    cellVivantesAutour = 0

    for xadd in range(-1, 2):
        for yadd in range(-1, 2):

            if x + xadd >=  taille and y + yadd >=  taille:
                if etatCell.get(x + xadd - taille, y + yadd - taille) == True:
                    cellVivantesAutour +=  1

            elif x + xadd >=  taille:
                if etatCell.get(x + xadd - taille, y + yadd) == True:
                    cellVivantesAutour +=  1

            elif y + yadd >=  taille:
                if etatCell.get(x + xadd, y + yadd - taille) == True:
                    cellVivantesAutour +=  1

            elif x !=  0 or y !=  0:
                if etatCell.get(x + xadd, y + yadd) == True:
                    cellVivantesAutour +=  1

    return cellVivantesAutour


def etapeSuivante():
    global etatCell, etatCell2

    #print("etapeSuivante")

    for x in range(taille):
        for y in range(taille):
            cellVivantesAutour = compteur(x, y)

            if cellVivantesAutour == 3:
                etatCell2[x, y] = True

            if cellVivantesAutour == 2 and etatCell.get(x, y) == True:
                etatCell2[x, y] = True

            else:
                etatCell2[x, y] = False

    etatCell = etatCell2


def actualisationFenetre():

    #print("actualisationFenetre")

    for x in range(taille):
        for y in range(taille):
            if etatCell.get(x, y) == True:
                Fenetre.grid_slaves(
                    row = y, column = x)[0].configure(bg = couleurVivant)

            else:
                Fenetre.grid_slaves(
                    row = y, column = x)[0].configure(bg = "light grey")


def changement():

    #print("changement")

    etapeSuivante()
    actualisationFenetre()


test = 0


def bouclePrincipale(pause = pause):
    global test

    print("bouclePrincipale")

    if test == 1:
        changement()
        #print("changement bouclePrincipale")

    test = 1

    #print("bouclePrincipale 2")

    Fenetre.after(pause * 1000, bouclePrincipale)


#Préparation

generation()
initialisationFenetre()

#Lancement

bouclePrincipale(10)

Fenetre.mainloop()

print("fin")

#
