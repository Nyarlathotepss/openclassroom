import pygame
from pygame.locals import KEYDOWN, QUIT, K_LEFT, K_RIGHT, K_UP, K_DOWN
from Element import Player, Dictionnary, Element

dict = Dictionnary()

pygame.init()

window = pygame.display.set_mode((300, 300))
fond = pygame.image.load("fond-gris.jpg").convert()
window.blit(fond, (0, 0))

dict.displayelement(window)

pygame.display.flip()

macgyver = Player(dict)
guardian = Player(dict)

continuer = 1
while continuer:

    position = macgyver.checkposition(dict)
    positionguardian = guardian.checkguardianposition(dict)

    for event in pygame.event.get():

        if event.type == QUIT:
            continuer = 0

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if dict.dict_labyrinthe[position[0] - 1, position[1]] != "w":
                    dict.dict_labyrinthe[position[0], position[1]] = "-"
                    dict.dict_labyrinthe[(position[0]) - 1, position[1]] = "m"
            if event.key == K_RIGHT:
                if dict.dict_labyrinthe[position[0] + 1, position[1]] != "w":
                    dict.dict_labyrinthe[position] = "-"
                    dict.dict_labyrinthe[(position[0]) + 1, position[1]] = "m"
            if event.key == K_DOWN:
                if dict.dict_labyrinthe[position[0], position[1] + 1] != "w":
                    dict.dict_labyrinthe[position] = "-"
                    dict.dict_labyrinthe[(position[0]), (position[1] + 1)] = "m"
            if event.key == K_UP:
                if dict.dict_labyrinthe[position[0], position[1] - 1] != "w":
                    dict.dict_labyrinthe[position] = "-"
                    dict.dict_labyrinthe[(position[0]), (position[1] - 1)] = "m"
            macgyver.checkobject(dict)

            position = macgyver.checkposition(dict)
            window.blit(fond, (0, 0))
            dict.displayelement(window)
            pygame.display.flip()
            print(position, positionguardian, macgyver.checkallobjects(), macgyver.listobjects)
        if position == positionguardian:
            if macgyver.checkallobjects() == False:
                continuer = 0
            else:
                fond2 = pygame.image.load("congrat.png").convert()
                window.blit(fond2, (0, 0))
                pygame.display.flip()
