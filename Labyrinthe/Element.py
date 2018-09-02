import pygame
import random


class Element:

    def __init__(self,positionx,positiony):
        self.positionx = positionx
        self.positiony = positiony


class Player:
    def __init__(self,dictionnary):
        self.positionx,self.positiony = self.checkposition(dictionnary)

    def checkposition(self,dictionnary):
        for cle, valeur in dictionnary.items():
            if valeur == "m":
                return cle

class Dictionnary:

    def __init__(self):
        '''By default my dictionnary is empty'''
        self.dict_labyrinthe = {}

    def generatedictionnary(self):
        ''' Generate a dictionnary with file.txt'''
        my_file = open("labyrinthe.txt", "r")
        text = my_file.read()

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
                self.dict_labyrinthe[key1, key2] = lettre
                key1 += 1
                if key1 == nb_lettre:
                    key1 = 0
                    key2 += 1

    def generateobject(self):
        '''generate 3 objects in random position in dictionnary'''
        list_empty_case = []
        for cle, valeur in self.dict_labyrinthe.items():
            if valeur == "-":
                list_empty_case.append(cle)
        position_object1 = random.choice(list_empty_case)
        position_object2 = random.choice(list_empty_case)
        position_object3 = random.choice(list_empty_case)
        self.dict_labyrinthe[position_object1] = "a"
        self.dict_labyrinthe[position_object2] = "b"
        self.dict_labyrinthe[position_object3] = "c"

    def lablist (self):
        '''create an object type list to show image in pygame( a revoir pour return list)'''
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

    def displaylabyrinthe (self):
        '''Display the blocks in window'''
        wall = pygame.image.load("wall.png").convert
        macgyver = pygame.image.load("MacGyver.png").convert
        needle = pygame.image.load("seringue.png").convert
        tube = pygame.image.load("tube_plastique.png").convert
        ether = pygame.image.load("ether.png").convert
        guardian = pygame.image.load("Gardien.png".).convert
        exit = pygame.image.load("wall.png").convert

        positiontocollapse = (0,0)

        for line in self.dict_labyrinthe:
            for lettre in line:
                if lettre == "w":
                    fenetre.blit(wall,(positiontocollapse))
                if lettre == "m":
                    fenetre.blit(macgyver,(positiontocollapse))
                if lettre == "a":
                    fenetre.blit(needle,(positiontocollapse))
                if lettre == "b":
                    fenetre.blit(tube,(positiontocollapse))
                if lettre == "c":
                    fenetre.blit(ether,(positiontocollapse))
                if lettre == "g"
                    fenetre.blit(wall,(positiontocollapse))
                elif lettre == "-":
                    continue

                positiontocollapse[1] += 20
            positiontocollapse[0] += 20