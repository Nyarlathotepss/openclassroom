import fonctions
import pygame
import random
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480),RESIZABLE)

fond = pygame.image.load("fond-gris.jpg").convert()

fenetre.blit(fond,(0,0))
pygame.display.flip()

continuer = 1
while continuer:
    for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
        if event.type == QUIT:  # Si un de ces événements est de type QUIT
            continuer = 0  # On arrête la boucle

'''
#On génére le labyrinthe en dictionnaire
dict_labyrinthe = fonctions.create_dict_labyrinthe()
print(dict_labyrinthe)

#On genere les 3 objets
 Nous allons generer un 2 eme dictionnaire qui ne contiendra que les tuples ayant pour valeur "-"
puis nous recupererons en random 3 postitions où nous placerons nos objets.

list_empty_case = []
for cle,valeur in dict_labyrinthe.items():
    if valeur == "-":
        list_empty_case.append(cle)
print(list_empty_case)

position_object1 = random.choice(list_empty_case)
position_object2 = random.choice(list_empty_case)
position_object3 = random.choice(list_empty_case)

print(position_object1,position_object2,position_object3)

dict_labyrinthe[position_object1] = "a"
dict_labyrinthe[position_object2] = "b"
dict_labyrinthe[position_object3] = "c"

print(dict_labyrinthe)



#perso = pygame.image.load("MacGyver.png").convert()

continu = 1
while continu:
# Ici on génére la boucle du labyrinthe
    play = True
    while play:

        ligne = str()
        list_lettre = []
        i = 0

        # Puis on l'affiche a l'utilisateur via l'aide d'une liste
        for lettre in dict_labyrinthe.values():
            list_lettre.append(lettre)
            i += 1
            if i > 15:
                ligne = "".join(list_lettre)
                print(ligne)
                ligne = None
                i = 0
                list_lettre = []

        # check de la position de mac gyver
        for cle,valeur in dict_labyrinthe.items():
            if valeur == "m":
                position = cle
        print(position)

        # Demande de direction a l'utilisateur qui va modifier la position de mc gyver
        move_input = input("saisir une direction:")
        if move_input == "q":
            dict_labyrinthe[position] = "-"
            dict_labyrinthe[(position[0]) - 1,position[1]] = "m"
        if move_input == "d":
            dict_labyrinthe[position] = "-"
            dict_labyrinthe[(position[0]) + 1,position[1]] = "m"
        if move_input == "s":
            dict_labyrinthe[position] = "-"
            dict_labyrinthe[(position[0]), (position[1] + 1)] = "m"
        if move_input =="z":
            dict_labyrinthe[position] = "-"
            dict_labyrinthe[(position[0]), (position[1] - 1)] = "m"

        print(dict_labyrinthe)
'''