import pygame
from pygame.locals import KEYDOWN, QUIT, K_LEFT, K_RIGHT, K_UP, K_DOWN
from Element import Player, Dictionnary, Element

'''create dictionnary then display window'''
d = Dictionnary()

pygame.init()

window = pygame.display.set_mode((300, 300))
fond = pygame.image.load("fond-gris.jpg").convert()
window.blit(fond, (0, 0))

d.displayelement(window)

pygame.display.flip()

'''game loop - waiting event'''
macgyver = Player(d)
guardian = Player(d)
continuer = 1
while continuer:

    position = macgyver.checkposition(d)
    positionguardian = guardian.checkguardianposition(d)

    for event in pygame.event.get():

        if event.type == QUIT:
            continuer = 0

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if d.dict_labyrinthe[position[0] - 1, position[1]] != "w":
                    d.dict_labyrinthe[position[0], position[1]] = "-"
                    d.dict_labyrinthe[(position[0]) - 1, position[1]] = "m"
            if event.key == K_RIGHT:
                if d.dict_labyrinthe[position[0] + 1, position[1]] != "w":
                    d.dict_labyrinthe[position] = "-"
                    d.dict_labyrinthe[(position[0]) + 1, position[1]] = "m"
            if event.key == K_DOWN:
                if d.dict_labyrinthe[position[0], position[1] + 1] != "w":
                    d.dict_labyrinthe[position] = "-"
                    d.dict_labyrinthe[(position[0]), (position[1] + 1)] = "m"
            if event.key == K_UP:
                if d.dict_labyrinthe[position[0], position[1] - 1] != "w":
                    d.dict_labyrinthe[position] = "-"
                    d.dict_labyrinthe[(position[0]), (position[1] - 1)] = "m"
            macgyver.checkobject(d)

            position = macgyver.checkposition(d)
            window.blit(fond, (0, 0))
            d.displayelement(window)
            pygame.display.flip()
            print(position, positionguardian, macgyver.checkallobjects(), macgyver.listobjects)
        if position == positionguardian:
            if macgyver.checkallobjects() == False:
                continuer = 0
            else:
                fond2 = pygame.image.load("congrat.png").convert()
                window.blit(fond2, (0, 0))
                pygame.display.flip()
