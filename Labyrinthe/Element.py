import pygame
import random

def Main():

    listtodisplay = []
    i = 0
    for letter in Dictionnary.dict_labyrinthe.values():
        for letter1 in Element.dictionnary.values(): # on accede a la variable dictionnary de Element ?
            if letter == letter1:
                fenetre.blit(Element.image)
                i += 1
                if i > 15:
                    listtodisplay.append("/ n")

class Element:

    dictionnary = {"w":"wall.png", "m":"MacGyver.png", "a":"seringue.png", "b":"tube_plastique.png", "c":"ether.png", "g":"Gardien.png", "-":"empty.png"}

    def __init__(self,positionx,positiony,letter):
        self.positionx = positionx
        self.positiony = positiony
        self.image = pygame.transform.scale(pygame.image.load(Element.dictionnary[letter]), [20,20])

    def display_element(self, fenetre):
        self.fenetre = pygame.display.set_mode((640, 480),RESIZABLE)

class Player:
    def __init__(self,dictionnary):
        self.positionx,self.positiony = self.checkposition(dictionnary)

    def checkposition(self,dictionnary):
        for cle, valeur in dictionnary.items():
            if valeur == "m":
                return cle

    def checkobject(self,dictionnary):
        while object != 3:
            if Player.checkposition() == self.position_object1(dictionnary):
                object += 1
            if Player.checkposition() == self.position_object2(dictionnary):
                object += 1
            if Player.checkposition() == self.position_object3(dictionnary):
                object += 1
'''if self.checkposition() == self. ou se trouve le gardien alors le jeu est fini sinon macgyber meurt'''



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
