import pygame
import random
from pygame.locals import *

#On génére le labyrinthe en dictionnaire
my_file = open("labyrinthe.txt", "r")
text = my_file.read()
dict_labyrinthe = {}
nb_lettre = 0  # Bloc pour compter le nombre de lettre dans une ligne
key1 = 0
key2 = 0
for lettre in text:
    nb_lettre += 1
    if lettre == "\n":
        nb_lettre -= 1  # Ici on enleve le saut de ligne \n du comptage de lettre
        break
for lettre in text:
    if lettre != "\n":
        dict_labyrinthe[key1,key2] = lettre
        key1 += 1
        if key1 == nb_lettre:
            key1 = 0
            key2 += 1

#On genere les 3 objets
'''Nous allons generer un 2 eme dictionnaire qui ne contiendra que les tuples ayant pour valeur "-"
puis nous recupererons en random 3 positions où nous plaçerons nos objets.'''
list_empty_case = []
for cle,valeur in dict_labyrinthe.items():
    if valeur == "-":
        list_empty_case.append(cle)
position_object1 = random.choice(list_empty_case)
position_object2 = random.choice(list_empty_case)
position_object3 = random.choice(list_empty_case)
dict_labyrinthe[position_object1] = "a"
dict_labyrinthe[position_object2] = "b"
dict_labyrinthe[position_object3] = "c"

# Ici commence l'interface graphique via pygame
pygame.init()
fenetre = pygame.display.set_mode((640, 480),RESIZABLE)
fond = pygame.image.load("fond-gris.jpg").convert()
fenetre.blit(fond,(0,0))

character = pygame.image.load("MacGyver.png").convert_alpha()
position_char = character.get_rect()

pygame.display.flip()

continuer = 1
while continuer:

    for event in pygame.event.get():  # On parcours la liste de tous les événements reçus

        if event.type == QUIT:  # Si un de ces événements est de type QUIT
            continuer = 0  # On arrête la boucle

        print("Please choice a direction")
        #pygame.event.wait()
        if event.type == K_LEFT:
            dict_labyrinthe[position] = "-"
            dict_labyrinthe[(position[0]) - 1, position[1]] = "m"
            position_char = position_char.move()
        if event.type == K_RIGHT:
            dict_labyrinthe[position] = "-"
            dict_labyrinthe[(position[0]) + 1, position[1]] = "m"
            position_char = position_char.move()
        if event.type == K_DOWN:
            dict_labyrinthe[position] = "-"
            dict_labyrinthe[(position[0]), (position[1] + 1)] = "m"
            position_char = position_char.move()
        if event.type == K_UP:
            dict_labyrinthe[position] = "-"
            dict_labyrinthe[(position[0]), (position[1] - 1)] = "m"
            position_char = position_char.move()

    # Creation du labyrinthe à afficher à l'aide d'une liste
    ligne = str()
    list_lettre = []
    i = 0
    for lettre in dict_labyrinthe.values():
        list_lettre.append(lettre)
        i += 1
        if i > 15:
            ligne = "".join(list_lettre)
            print(ligne)
            ligne = None
            i = 0
            list_lettre = []
