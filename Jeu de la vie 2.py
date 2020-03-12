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
etatCell = []  #map avec état cell à l'étape n
etatCell2 = []  #map avec état cell à l'étape n+1
pause = 3
random = False

#Fenetre Principale
Fenetre = Tk()
Fenetre.title("Jeu de la Vie by Marius")

#Génération


def generation():

    for x in range(taille):
        etatCell.append([])
        etatCell2.append([])

        for y in range(taille):
            etatCell[x].append([])
            etatCell2[x].append([])

            if randint(0, 100) < poucentageVivant:
                etatCell[x][y] = True
            else:
                etatCell[x][y] = False


#Fenetre


def initialisationFenetre():

    for x in range(taille):
        for y in range(taille):
            if etatCell[x][y] == True:
                Label(
                    Fenetre,
                    text="   ",
                    relief=GROOVE,
                    borderwidth=1,
                    bg="chartreuse").grid(
                        row=y, column=x, sticky="news")
            else:
                Label(
                    Fenetre,
                    text="   ",
                    relief=GROOVE,
                    borderwidth=1,
                    bg="light grey").grid(
                        row=y, column=x, sticky="news")


def compteur(x, y):

    cellVivantesAutour = 0

    for xadd in range(-1, 2):
        for yadd in range(-1, 2):

            if x + xadd >= taille and y + yadd >= taille:
                if etatCell[x + xadd - taille][y + yadd - taille] == True:
                    cellVivantesAutour += 1

            elif x + xadd >= taille:
                if etatCell[x + xadd - taille][y + yadd] == True:
                    cellVivantesAutour += 1

            elif y + yadd >= taille:
                if etatCell[x + xadd][y + yadd - taille] == True:
                    cellVivantesAutour += 1

            elif i != 0 or j != 0:
                if etatCell[x + xadd][y + yadd] == True:
                    cellVivantesAutour += 1

    return cellVivantesAutour


def etapeSuivante():
    global etatCell, etatCell2

    for x in range(taille):
        for y in range(taille):
            cellVivantesAutour = compteur(x, y)

            if cellVivantesAutour == 3:
                etatCell2[x][y] == True

            if cellVivantesAutour == 2 and etatCell[x][y] == True:
                etatCell2[x][y] == True

            else:
                etatCell2[x][y] = False

    etatCell = etatCell2


def actualisationFenetre():

    for x in range(taille):
        for y in range(taille):
            if etatCell[x][y] == True:
                Fenetre.grid_slaves(
                    row=y, column=x)[0].configure(bg="chartreuse")

            else:
                Fenetre.grid_slaves(
                    row=y, column=x)[0].configure(bg="light grey")


def changement():
    etapeSuivante()
    actualisationFenetre()


test = 0


def bouclePrincipale():
    global test

    if test == 1:
        changement()

    test = 1

    Fenetre.adter(pause * 1000, boucle)


#Préparation

generation()
initialisationFenetre()

#Lancement

bouclePrincipale

Fenetre.mainloop

print("fin")

#
