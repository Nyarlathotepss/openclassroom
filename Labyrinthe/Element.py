import pygame
import random

class Element:

    dictionnary = {"w":"wall.png", "m":"MacGyver.png", "a":"seringue.png", "b":"tube_plastique.png", "c":"ether.png", "g":"Gardien.png", "-":"empty.png"}

    def __init__(self,letter):
        self.position = []
        self.letter = letter
        self.image = pygame.transform.scale(pygame.image.load(Element.dictionnary[letter]), [20,20])

    def insertposition(self,positionx,positiony):
        self.position.append([positionx,positiony])




class Player:

    def __init__(self,dictionnary):
        self.positionx,self.positiony = self.checkposition(dictionnary)
        self.listobjects = set()

    def checkposition(self,dictionnary):
        for cle, valeur in dictionnary.items():
            if valeur == "m":
                return cle

    def checkobject(self,dictionnary):

        if self.checkposition() == dictionnary.object1[0]: # j'apelle un object dictionnary qui contient object1 (lui meme une liste)
            self.listobjects.add(dictionnary.object1[1])
        if self.checkposition() == dictionnary.object2[0]:
            self.listobjects.add(dictionnary..object2[1])
        if self.checkposition() == dictionnary.object3[0]:
            self.listobjects.add(dictionnary.object3[1])

    def checkallobjects(self):

        if len(self.listobjects) == 3:
            return True
        else:
            return False



class Dictionnary:

    def __init__(self):
        '''By default my dictionnary is empty'''
        self.dict_labyrinthe = {}
        self.object1 = []
        self.object2 = []
        self.object3 = []
        self.generatedictionnary()
        self.generateobject()

    def generatedictionnary(self):
        ''' Generate a dictionnary with file.txt'''
        my_file = open("labyrinthe.txt", "r")
        text = my_file.read()

        nb_lettre = 0  # Bloc pour compter le nombre de lettres dans une ligne
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
        self.object1.append(random.choice(list_empty_case)
        self.object2.append(random.choice(list_empty_case)
        self.object3.append(random.choice(list_empty_case)
        self.dict_labyrinthe[self.object1[0]] = "a"
        self.object1.append("a")
        self.dict_labyrinthe[self.object2[0]] = "b"
        self.object2.append("b")
        self.dict_labyrinthe[self.object3[0]] = "c"
        self.object3.append("c")

    def display_element(self, fenetre):
        self.fenetre =