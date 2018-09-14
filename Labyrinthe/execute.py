import pygame
from Element import *
from pygame.locals import *

dict = Dictionnary()

# Ici commence l'interface graphique via pygame
pygame.init()

window = pygame.display.set_mode((300, 300),RESIZABLE)
fond = pygame.image.load("fond-gris.jpg").convert()
window.blit(fond,(0,0))

dict.display_element(window)

pygame.display.flip()

continuer = 1
while continuer:

    macgyver = Player(dict)
    guardian = Player(dict)
    position = macgyver.checkposition(dict)
    positionguardian = guardian.checkguardianposition(dict)

    for event in pygame.event.get():  # On parcours la liste de tous les événements reçus

        if event.type == QUIT:  # Si un de ces événements est de type QUIT
            continuer = 0  # On arrête la boucle

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                dict.dict_labyrinthe[position[0],position[1]] = "-"
                dict.dict_labyrinthe[(position[0]) - 1, position[1]] = "m"
            if event.key == K_RIGHT:
                dict.dict_labyrinthe[position] = "-"
                dict.dict_labyrinthe[(position[0]) + 1, position[1]] = "m"
            if event.key == K_DOWN:
                dict.dict_labyrinthe[position] = "-"
                dict.dict_labyrinthe[(position[0]), (position[1] + 1)] = "m"
            if event.key == K_UP:
                dict.dict_labyrinthe[position] = "-"
                dict.dict_labyrinthe[(position[0]), (position[1] - 1)] = "m"
            window.blit(fond, (0, 0))
            dict.display_element(window)
            pygame.display.flip()
        if dict.dict_labyrinthe[position] == positionguardian:
            if macgyver.checkallobjects == False:
                continuer = 0



