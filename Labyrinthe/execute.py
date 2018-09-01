import pygame
import random
from Element import *
from pygame.locals import *

dict = Dictionnary()
dict.generatedictionnary()
dict.generateobject()

# Ici commence l'interface graphique via pygame
pygame.init()

fenetre = pygame.display.set_mode((640, 480),RESIZABLE)
fond = pygame.image.load("fond-gris.jpg").convert()
fenetre.blit(fond,(0,0))

pygame.display.flip()

continuer = 1
while continuer:

    macgyver = Player(dict.dict_labyrinthe)# A revoir !!!!!
    position = (macgyver.positionx,macgyver.positiony)

    for event in pygame.event.get():  # On parcours la liste de tous les événements reçus

        if event.type == QUIT:  # Si un de ces événements est de type QUIT
            continuer = 0  # On arrête la boucle

        if event.type == K_LEFT:
            dict.dict_labyrinthe[position] = "-"
            dict.dict_labyrinthe[(position[0]) - 1, position[1]] = "m"
        if event.type == K_RIGHT:
            dict.dict_labyrinthe[position] = "-"
            dict.dict_labyrinthe[(position[0]) + 1, position[1]] = "m"
        if event.type == K_DOWN:
            dict.dict_labyrinthe[position] = "-"
            dict.dict_labyrinthe[(position[0]), (position[1] + 1)] = "m"
        if event.type == K_UP:
            dict.dict_labyrinthe[position] = "-"
            dict.dict_labyrinthe[(position[0]), (position[1] - 1)] = "m"

        dict.lablist()
        dict.displaylabyrinthe()

        pygame.display.flip()
